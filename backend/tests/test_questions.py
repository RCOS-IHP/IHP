from .conftest import client
from src.models import QuestionType, Choice, Answer

class TestQuestions:
    def test_add_multiple_choice_question(self):
        question_text = "Sample **Question**?"
        choices = [Choice(text="Choice 1", choice_id=1), Choice(text="Choice 2", choice_id=2), Choice(text="Choice 3", choice_id=3), Choice(text="Choice 4", choice_id=4)]
        answer = Answer(correct_choice_ids=[3])
        question_data = {"type": QuestionType.multiple_choice.value, "question_text": question_text, "choices": [model.dict() for model in choices], "answer": answer.dict()}
        response = client.post("/question", json=question_data)
        json_response = response.json()
        assert response.status_code == 200
        assert json_response["type"] == QuestionType.multiple_choice.value
        assert json_response["question_text"] == question_text
        assert json_response["choices"] == [model.dict() for model in choices]
        assert json_response["answer"] == answer
        assert json_response["id"]
