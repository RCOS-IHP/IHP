from fastapi import HTTPException
from ...models import User, UserPassword
from ...main import app
from pydantic import BaseModel, Field
from .auth_common import generate_new_token, Tokens, hasher

class SignupRequest(BaseModel):
    username: str = Field(min_length=3, max_length=100)
    password: str = Field(min_length=8, max_length=100)
    email: str = Field(min_length=5, max_length=100)

@app.post("/auth/signup", response_model=Tokens)
async def signup(login_info: SignupRequest):
    if await User.objects.get_or_none(username=login_info.username):
        raise HTTPException(status_code=400, detail="Username already exists.")
    if await User.objects.get_or_none(email=login_info.email):
        raise HTTPException(status_code=400, detail="Email already exists.")
    new_user = await User.objects.create(username=login_info.username, email=login_info.email)
    await UserPassword.objects.create(user=new_user, hashed_password=hasher.hash(login_info.password))
    return await generate_new_token(new_user.id)