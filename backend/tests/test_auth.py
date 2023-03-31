from .conftest import client
from src.routes.auth.login import LoginRequest
from src.routes.auth.signup import SignupRequest

class TestAuth:
    def test_signup(self):
        email = "test@test.com"
        username = "_test"
        password="asdfghjkl"
        signup_request = SignupRequest(
            email=email,
            username=username,
            password=password
        )
        response = client.post("/auth/signup", json=signup_request.dict())
        assert response.status_code == 200
        json_response = response.json()
        assert json_response["access_token"]
        assert json_response["refresh_token"]
    
    def test_login(self):
        username = "_test"
        password="asdfghjkl"
        login_request = LoginRequest(
            username=username,
            password=password
        )
        response = client.post("/auth/login", json=login_request.dict())
        assert response.status_code == 200
        json_response = response.json()
        assert json_response["access_token"]
        assert json_response["refresh_token"]