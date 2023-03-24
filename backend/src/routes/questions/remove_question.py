from fastapi import HTTPException
from ...models import Question
from ...main import app

@app.delete("/question/{question_id}", status_code=204)
async def remove_question(question_id: int):
    question = await Question.objects.get_or_none(id=question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    await question.delete()
    return None