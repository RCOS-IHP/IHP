from secrets import token_urlsafe
from .conftest import client
from src.routes.auth.login import LoginRequest
from src.routes.auth.signup import SignupRequest


class TestAuth:
    random_suffix = token_urlsafe(8)

    def test_signup(self):
        email = f"test{self.random_suffix}@test.com"
        username = f"_test{self.random_suffix}"
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
    
    def test_login_username(self):
        username = f"_test{self.random_suffix}"
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
    
    def test_login_email(self):
        email = f"test{self.random_suffix}@test.com"
        password="asdfghjkl"
        login_request = LoginRequest(
            email=email,
            password=password
        )
        response = client.post("/auth/login", json=login_request.dict())
        assert response.status_code == 200
        json_response = response.json()
        assert json_response["access_token"]
        assert json_response["refresh_token"]
