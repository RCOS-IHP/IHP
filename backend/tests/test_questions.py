from .conftest import client, encoder_for_enums
from src.models import QuestionType, Choice, Answer
from src.routes.questions.add_question import QuestionRequest

class TestQuestions:
    def test_add_multiple_choice_question(self):
        question_text = "Sample **Question**?"
        choices = [Choice(text="Choice 1", choice_id=1), Choice(text="Choice 2", choice_id=2), Choice(text="Choice 3", choice_id=3), Choice(text="Choice 4", choice_id=4)]
        answer = Answer(correct_choice_ids=[3])
        question_data = QuestionRequest(type=QuestionType.multiple_choice, question_text=question_text, choices=choices, answer=answer)
        response = client.post("/question", content=question_data.json(encoder=encoder_for_enums), headers={"Content-Type": "application/json"})
        assert response.status_code == 200
        json_response = response.json()
        assert json_response["type"] == QuestionType.multiple_choice.value
        assert json_response["question_text"] == question_text
        assert json_response["choices"] == [model.dict() for model in choices]
        assert json_response["answer"] == answer
        assert json_response["id"]

    def test_short_answer_question(self):
        question_text = "Sample **Question**?"
        answer = Answer(text="Answer")
        question_data = QuestionRequest(type=QuestionType.short_answer, question_text=question_text, choices=None, answer=answer)
        response = client.post("/question", content=question_data.json(encoder=encoder_for_enums), headers={"Content-Type": "application/json"})
        assert response.status_code == 200
        json_response = response.json()
        assert json_response["type"] == QuestionType.short_answer.value
        assert json_response["question_text"] == question_text
        assert json_response["choices"] is None
        assert json_response["answer"] == answer
        assert json_response["id"]

    def test_add_select_multiple_question(self):
        question_text = "Sample **Question**?"
        choices = [Choice(text="Choice 1", choice_id=1), Choice(text="Choice 2", choice_id=2), Choice(text="Choice 3", choice_id=3), Choice(text="Choice 4", choice_id=4)]
        answer = Answer(correct_choice_ids=[1,3])
        question_data = QuestionRequest(type=QuestionType.select_multiple, question_text=question_text, choices=choices, answer=answer)
        response = client.post("/question", content=question_data.json(encoder=encoder_for_enums), headers={"Content-Type": "application/json"})
        assert response.status_code == 200
        json_response = response.json()
        assert json_response["type"] == QuestionType.select_multiple.value
        assert json_response["question_text"] == question_text
        assert json_response["choices"] == [model.dict() for model in choices]
        assert json_response["answer"] == answer
        assert json_response["id"]

    def test_add_select_one_question(self):
        question_text = "Sample **Question**?"
        choices = [Choice(text="Choice 1", choice_id=1), Choice(text="Choice 2", choice_id=2), Choice(text="Choice 3", choice_id=3), Choice(text="Choice 4", choice_id=4)]
        answer = Answer(correct_choice_ids=[1,3])
        question_data = QuestionRequest(type=QuestionType.select_one, question_text=question_text, choices=choices, answer=answer)
        response = client.post("/question", content=question_data.json(encoder=encoder_for_enums), headers={"Content-Type": "application/json"})
        assert response.status_code == 200
        json_response = response.json()
        assert json_response["type"] == QuestionType.select_one.value
        assert json_response["question_text"] == question_text
        assert json_response["choices"] == [model.dict() for model in choices]
        assert json_response["answer"] == answer
        assert json_response["id"]
