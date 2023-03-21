import secrets
from fastapi import HTTPException
from pydantic import BaseModel
from datetime import datetime, timezone
from ...main import app
from ...models import User, UserTokens
from argon2 import PasswordHasher

hasher = PasswordHasher()

class Tokens(BaseModel):
    access_token: str
    refresh_token: str

class AccessTokenDB:
    def __init__(self):
        self.tokens: dict[str, datetime] = {}
        self.user_id_token_map: dict[int, list[str]] = {}

    def add_token(self, token: str, user_id: int):
        assert token not in self.tokens, "Tried to add duplicate token."
        # Make it so that every token is valid for 1 hour from the time it was created.
        self.tokens[token] = datetime.now(tz=timezone.utc) + datetime.timedelta(hours=1)
        self.user_id_token_map[user_id].append(token)

    def token_valid(self, token: str):
        exists = token in self.tokens
        if exists:
            # If the token exists, checks that there is less than 10 seconds left until it expires.
            time_valid = datetime.now(tz=timezone.utc) - self.tokens[token] > datetime.timedelta(seconds=10)
            if time_valid:
                return True
            else:
                # If the token is expired, remove it from the list of valid tokens so we do not have to do the expensive check with datetimes.
                self.tokens.pop(token)
                return False
        return False

    def invalid_all_user_tokens(self, user_id: int):
        """Invalidate all tokens for a user. This is useful if they change their password for example.

        :param user_id: The user id to invalidate all tokens for.
        """
        for token in self.user_id_token_map[user_id]:
            self.tokens.pop(token, None)
        self.user_id_token_map.pop(user_id)

app.state.access_token_db: AccessTokenDB = AccessTokenDB()

def generate_new_token(length: int=32) -> str:
    """Generate a new token.

    :return: The new token.
    """
    return secrets.token_urlsafe(length)

async def get_new_token(user_id: int | None = None, refresh_token: str | None = None) -> Tokens:
    """Get a new access token for a user.

    :param user_id: The user id to get a new token for, if no refresh token is provided.
    :param refresh_token: The refresh token to get a new access token for.
    :return: The new access token and refresh token.
    """
    if refresh_token:
        refresh_token_obj = await UserTokens.objects.get_or_none(token=refresh_token)
        if not refresh_token_obj:
            raise HTTPException(status_code=401, detail="Invalid refresh token.")
        user_id = refresh_token_obj.user.id
        if datetime.now(tz=timezone.utc) - refresh_token_obj.expiry.astimezone(timezone.utc) < datetime.timedelta(minutes=5):
            raise HTTPException(status_code=401, detail="Expired refresh token.")
        new_token = generate_new_token()
        app.state.access_token_db.add_token(new_token, user_id)
        return Tokens(access_token=new_token, refresh_token=refresh_token)
    else:
        if not user_id:
            raise HTTPException(status_code=400, detail="No user id provided.")
        new_token = generate_new_token()
        new_refresh_token = generate_new_token(length=64)
        app.state.access_token_db.add_token(new_token, user_id)
        await UserTokens.objects.create(user_id=user_id, token=new_refresh_token, expiry=datetime.now(tz=timezone.utc) + datetime.timedelta(days=30))
        return Tokens(access_token=new_token, refresh_token=refresh_token)