from typing import Annotated
from datetime import timedelta, datetime


from fastapi import HTTPException, Header
from ...models import Choice, QuestionType, Question, Answer, User, AuditLog
from ...main import app
from pydantic import BaseModel
from ...utils import convert_to_json
from ..auth.auth_common import get_user_or_401

class QuestionRequest(BaseModel):
    type: QuestionType
    question_text: str
    choices: list[Choice] | None
    answer: Answer

@app.post("/question", response_model=Question)
async def add_question(authorization: Annotated[str, Header()], question: QuestionRequest):
    """This handles the request to add questions to the database"""
    user = await get_user_or_401(authorization)
    question_model = Question(
        type=question.type.value,
        question_text=question.question_text,
        choices=convert_to_json(question.choices),
        answer=convert_to_json(question.answer),
        creator=user
    )

    if question.type is QuestionType.short_answer:
        if question.choices is not None:
            raise HTTPException(status_code=400, detail="Short answer questions do not need choices")
    else:
        if question.choices is None:
            raise HTTPException(status_code=400, detail="Choices must be provided for multiple choice questions")
        if question.answer.text is not None or question.answer.correct_choice_ids is None:
            raise HTTPException(status_code=400, detail="Answer format must be a list of integers")
        if question.type is QuestionType.multiple_choice:
            if len(question.answer.correct_choice_ids) != 1:
                raise HTTPException(status_code=400, detail="Answers list must have a length of 1")
        else:
            if len(question.answer.correct_choice_ids) == 1:
                raise HTTPException(status_code=400, detail="For this question type, there must be multiple correct answers")

    await question_model.save()
    add_question_audit_log(question_model, user)
    return question_model

async def add_question_audit_log(question: Question, user: User):
    print(question)
    event_data = {
        "question_text": question.question_text,
        "choices": convert_to_json(question.choices),
        "answer": convert_to_json(question.answer),
        "type": question.type
    }
    auditAddition = AuditLog(
        causing_user = user,
        #I don't like this, it wastes a lot of space. May be trimmed down
        event_data  = event_data,
        event_type = "add_question",
        effected_id = question.id,
        created_on = datetime.now(),
        expiry     = datetime.utcnow() + timedelta(days=365)
    )
    auditAddition.save()