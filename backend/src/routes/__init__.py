from .root import root
from .questions.add_question import add_question
from .questions.get_question import get_question

routes = [
    root,
    add_question,
    get_question
]