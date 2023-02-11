from fastapi import HTTPException
from ...models import Question
from ...main import app

@app.get("/question/{question_id}", response_model=Question)
async def get_question(question_id: int):
    question = await Question.objects.get_or_none(id=question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return question