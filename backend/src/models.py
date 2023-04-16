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

class User(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=100, unique=True, nullable=False)
    email: str = ormar.String(max_length=100, unique=True, nullable=False)
    email_verified: bool = ormar.Boolean(default=False)
    created_on: datetime.datetime = ormar.DateTime(default=lambda: datetime.datetime.now(datetime.timezone.utc), timezone=True, nullable=False)

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
    created_on: datetime.datetime = ormar.DateTime(default=lambda: datetime.datetime.now(datetime.timezone.utc), timezone=True, nullable=False)
    creator: User = ormar.ForeignKey(User, nullable=False)

class UserPassword(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    user: User = ormar.ForeignKey(User)
    hashed_password: str = ormar.LargeBinary(max_length=97, represent_as_base64_str=False, nullable=False)

class UserTokens(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    user: User = ormar.ForeignKey(User)
    token: str = ormar.String(max_length=100, nullable=False, unique=True)
    created_on: datetime.datetime = ormar.DateTime(default=lambda: datetime.datetime.now(datetime.timezone.utc), timezone=True, nullable=False)
    expiry: datetime.datetime = ormar.DateTime(nullable=False)

class EmailVerificationTokens(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    user: User = ormar.ForeignKey(User)
    token: str = ormar.String(max_length=100, nullable=False, unique=True)
    created_on: datetime.datetime = ormar.DateTime(default=lambda: datetime.datetime.now(datetime.timezone.utc), timezone=True, nullable=False)
    expiry: datetime.datetime = ormar.DateTime(nullable=False)

class SignInAuditLog(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    user: User = ormar.ForeignKey(User)
    ip_address: str = ormar.String(max_length=100, nullable=False)
    created_on: datetime.datetime = ormar.DateTime(default=lambda: datetime.datetime.now(datetime.timezone.utc), timezone=True, nullable=False)

class AuditLog(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    event_id: int = ormar.BigInteger(primary_key=True)
    effected_id: int = ormar.BigInteger(nullable=True)
    causing_user: User | None = ormar.ForeignKey(User, nullable=True)
    event_type: str = ormar.String(max_length=100, nullable=False)
    event_data: dict | None = ormar.JSON(nullable=True)
    created_on: datetime.datetime = ormar.DateTime(default=lambda: datetime.datetime.now(datetime.timezone.utc), timezone=True, nullable=False)
    expiry: datetime.datetime = ormar.DateTime(nullable=False)

class Course(ormar.Model):
    class Meta:
        database = database
        metadata = metadata
    
    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100, nullable=False, unique=True)
    descript: str = ormar.String(max_length=500)
    
class OwnerType(enum.Enum):
    """Question type enum. Determines what type the question is."""
    creator = 1
    admin = 2
    participant = 3

class CourseParticipant(ormar.Model):
    class Meta:
        database = database
        metadata = metadata
    
    id: int = ormar.Integer(primary_key=True)
    uid: User = ormar.ForeignKey(User)
    cid: Course = ormar.ForeignKey(Course)
    type: int = ormar.SmallInteger(nullable=False, choices=list(QuestionType))

class Assignment(ormar.Model):
    class Meta:
        database = database
        metadata = metadata
    
    id: int = ormar.Integer(primary_key=True)
    cid: Course = ormar.ForeignKey(Course)
    name: str = ormar.String(max_length=100, nullable=False)
    description: str = ormar.String(nullable=False, max_length=500)
    dueDate: datetime.datetime = ormar.DateTime(nullable=False)

class AssignmentMember(ormar.Model): 
    class Meta:
        database = database
        metadata = metadata
    
    id: int = ormar.Integer(primary_key=True)
    aid: Assignment = ormar.ForeignKey(Assignment)
    qid: Question   = ormar.ForeignKey(Question)
    name: str = ormar.String(max_length=100, nullable=False)
    description: str = ormar.String(nullable=False, max_length=500)
    dueDate: datetime.datetime = ormar.DateTime(nullable=False)
    pointValue: int = ormar.Integer(nullable=True)

