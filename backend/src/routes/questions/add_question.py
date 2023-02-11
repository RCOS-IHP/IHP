from fastapi import HTTPException
from ...models import Choice, QuestionType, Question
from ...main import app
from pydantic import BaseModel

class QuestionRequest(BaseModel):
    type: int
    question_text: str
    choices: list[Choice] | None
    answer: str | int

@app.post("/question", response_model=Question)
async def add_question(question: QuestionRequest):
    question = Question(
        type=question.type,
        question_text=question.question_text,
        choices=question.choices,
        answer=question.answer
    )
    if question.type in [QuestionType.mutliple_choice, QuestionType.select_multiple]:
        if question.choices is None:
            raise HTTPException(status_code=400, detail="Choices must be provided for multiple choice questions")
        if question.answer not in [choice.choice_id for choice in question.choices]:
            raise HTTPException(status_code=400, detail="Answer must be a valid choice")
        if not isinstance(question.answer, int):
            raise HTTPException(status_code=400, detail="Answer must be an integer for choice questions")
    await question.save()
    return question
