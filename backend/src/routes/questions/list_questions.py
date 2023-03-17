from ...models import Question
from ...main import app

from fastapi_pagination import Page
from fastapi_pagination.ext.ormar import paginate

@app.get("/question", response_model=Page[Question])
async def list_questions():
    return await paginate(Question.objects)