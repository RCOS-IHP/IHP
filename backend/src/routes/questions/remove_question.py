from fastapi import HTTPException, Header
from datetime import timedelta, datetime
from pydantic import BaseModel
from typing import Annotated

from ..auth.auth_common import get_user_or_401
from ...models import Question, User
from ...main import app
from ...utils import convert_to_json

@app.delete("/question/{question_id}", status_code=204)
async def remove_question(authorization: Annotated[str, Header()], question_id: int):
    """This handles the request to add questions to the database"""
    user = await get_user_or_401(authorization)
    question = await Question.objects.get_or_none(id=question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    await question.delete()
    remove_question_audit_log(question, user)
    return None

async def remove_question_audit_log(question: Question, user: User):
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
        event_type = "remove_question",
        effected_id = question.id,
        created_on = datetime.now(),
        expiry     = datetime.utcnow() + timedelta(days=365)
    )
    auditAddition.save()