import ormar
import pydantic
import enum
from .main import database, metadata


class QuestionType(enum.Enum):
    """Question type enum. Determines what type the question is."""
    multiple_choice = 1
    short_answer = 2
    select_multiple = 3

class Choice(pydantic.BaseModel):
    text: str
    choice_id: int

class Answer(pydantic.BaseModel):
    """The answer class, this is what we receive when a answer is sent"""
    text: str | None = None
    correct_choice_id: int | None = None


class Question(ormar.Model):
    """The actual question class, basically records the type id and choices"""
    class Meta:
        database = database
        metadata = metadata
    id: int = ormar.Integer(primary_key=True)
    type: int = ormar.SmallInteger(nullable=False, choices=list(QuestionType))
    question_text: str = ormar.Text(nullable=False)
    choices: list[Choice] | None = ormar.JSON(nullable=True)
    answer: Answer = ormar.JSON(nullable=False)

