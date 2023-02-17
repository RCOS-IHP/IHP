from .conftest import client
from src.models import QuestionType, Choice

class TestQuestions:
    def test_add_multiple_choice_question(self):
        question_text = "Sample **Question**?"
        choices = [Choice(text="Choice 1", choice_id=1), Choice(text="Choice 2", choice_id=2), Choice(text="Choice 3", choice_id=3), Choice(text="Choice 4", choice_id=4)]
        answer = 3
        question_data = {"type": QuestionType.mutliple_choice.value, "question_text": question_text, "choices": [model.json() for model in choices], "answer": answer}
        response = client.post("/question", json=question_data)
        assert response.status_code == 200
        json_response = response.json()
        assert json_response["type"] == QuestionType.mutliple_choice.value
        assert json_response["question_text"] == question_text
        assert json_response["choices"] == [model.json() for model in choices]
        assert json_response["answer"] == answer
        assert json_response["id"]