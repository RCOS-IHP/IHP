from .root import root
from .questions.add_question import add_question
from .questions.get_question import get_question
from .questions.list_questions import list_questions

routes = [
    root,
    add_question,
    get_question,
    list_questions,
]