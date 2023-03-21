from fastapi import HTTPException
from ...models import User, UserPassword
from ...main import app
from pydantic import BaseModel, Field
from .auth_common import get_new_token, Tokens, hasher, validate_and_normalize_email

class LoginRequest(BaseModel):
    username: str | None = Field(min_length=3, max_length=100, default=None)
    password: str = Field(min_length=8, max_length=100)
    email: str | None = Field(min_length=5, max_length=100, default=None)

@app.post("/auth/login", response_model=Tokens)
async def login(login_info: LoginRequest):
    if login_info.username is None and login_info.email is None:
        raise HTTPException(status_code=400, detail="Either username or email is required.")
    if login_info.username is not None:
        user = await User.objects.get_or_none(username=login_info.username)
    else:
        login_info.email = validate_and_normalize_email(login_info.email)
        user = await User.objects.get_or_none(email=login_info.email)
    if user is None:
        raise HTTPException(status_code=400, detail="Username or email does not exist.")
    user_password = await UserPassword.objects.get_or_none(user=user)
    if user_password is None:
        raise HTTPException(status_code=400, detail="User does not have a password.")
    if not hasher.verify(user_password.hashed_password, login_info.password):
        raise HTTPException(status_code=400, detail="Incorrect password.")
    return await get_new_token(user)