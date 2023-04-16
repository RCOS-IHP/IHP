from .questions.add_question import add_question
from .questions.remove_question import remove_question
from .questions.get_question import get_question
from .questions.list_questions import list_questions
from .questions.edit_question import edit_question
from .auth.login import login
from .auth.signup import signup
from .courses.add_course import add_course
from .courses.get_course import get_course
from .courses.add_course_participant import add_course_participant



routes = [
    add_question,
    remove_question,
    get_question,
    list_questions,
    edit_question,
    login,
    signup,
    add_course,
    get_course,
    add_course_participant
]