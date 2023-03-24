from .root import root
from .questions.add_question import add_question
from .questions.remove_question import remove_question
from .questions.get_question import get_question
from .questions.list_questions import list_questions
from .auth.login import login
from .auth.signup import signup

routes = [
    root,
    add_question,
    remove_question,
    get_question,
    list_questions,
    login,
    signup,
]