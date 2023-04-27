from fastapi import HTTPException, Header
from typing import Annotated

from ...models import Question, User
from ...main import app
from ..auth.auth_common import get_user_or_401


@app.get("/question/{question_id}", response_model=Question)
async def get_question(authorization: Annotated[str, Header()], question_id: int):
    user = await get_user_or_401(authorization)
    question = await Question.objects.get_or_none(id=question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return question