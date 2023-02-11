import ormar
import pydantic
import enum
from .main import database, metadata

class QuestionType(enum.Enum):
    mutliple_choice = 1
    short_answer = 2
    select_multiple = 3

class Choice(pydantic.BaseModel):
    text: str
    choice_id: int

class Question(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    type: int = ormar.SmallInteger(nullable=False, choices=list(QuestionType))
    question_text: str = ormar.Text(nullable=False)
    choices: list[Choice] | None = ormar.JSON(nullable=True)
    answer: str | int = ormar.JSON(nullable=False)