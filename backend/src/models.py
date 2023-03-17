import ormar
import pydantic
import datetime
import enum
from .main import database, metadata


class QuestionType(enum.Enum):
    """Question type enum. Determines what type the question is."""
    multiple_choice = 1
    short_answer = 2
    select_multiple = 3
    select_one = 4

class Choice(pydantic.BaseModel):
    text: str
    choice_id: int

class Answer(pydantic.BaseModel):
    """The answer class, this is what we receive when a answer is sent"""
    text: str | None = None
    correct_choice_ids: list[int] | None = None


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


class User(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=100, unique=True, nullable=False)
    email: str = ormar.String(max_length=100, unique=True, nullable=False)

class UserPassword(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    user: User = ormar.ForeignKey(User)
    hashed_password: str = ormar.LargeBinary(max_length=97, represent_as_base64_str=False, nullable=False)
    salt: str = ormar.String(min_length=16, max_length=16, nullable=False)

class UserTokens(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    user: User = ormar.ForeignKey(User)
    token: str = ormar.String(max_length=100, nullable=False, unique=True)
    expiry: datetime.datetime = ormar.DateTime(nullable=False)