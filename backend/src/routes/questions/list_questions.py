from ...models import Question
from ...main import app

@app.get("/question", response_model=list[Question])
async def list_questions():
    return await Question.objects.all()