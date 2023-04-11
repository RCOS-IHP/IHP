import secrets
from fastapi import HTTPException, Request
from pydantic import BaseModel
from datetime import datetime, timezone, timedelta
from ...main import app
from ...models import User, UserTokens
from argon2 import PasswordHasher
from email_validator import validate_email, EmailNotValidError
from collections import defaultdict
from async_lru import alru_cache

hasher = PasswordHasher()

class Tokens(BaseModel):
    access_token: str
    refresh_token: str

@alru_cache(maxsize=2**10)
async def get_user_from_user_id(user_id: int) -> User:
    return await User.objects.get(id=user_id)

class AccessTokenDB:
    def __init__(self):
        self.tokens: dict[str, datetime] = {}
        self.user_id_token_map: defaultdict[int, list[str]] = defaultdict(list)
        self.token_to_user_id_map: dict[str, int] = {}

    def add_token(self, token: str, user_id: int):
        assert token not in self.tokens, "Tried to add duplicate token."
        # Make it so that every token is valid for 1 hour from the time it was created.
        self.tokens[token] = datetime.now(tz=timezone.utc) + timedelta(hours=1)
        self.user_id_token_map[user_id].append(token)
        self.token_to_user_id_map[token] = user_id
        assert token in self.tokens, "Token was not added to the token list."
        assert user_id in self.user_id_token_map, "User id was not added to the user id list."
        assert token in self.user_id_token_map[user_id], "Token was not added to the user id list."
        assert token in self.token_to_user_id_map, "User id was not added to the token to user id map."

    def token_valid(self, token: str):
        exists = token in self.tokens
        if exists:
            # If the token exists, checks that there is less than 10 seconds left until it expires.
            time_valid = self.tokens[token] - datetime.now(tz=timezone.utc) > timedelta(seconds=10)
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

    def prune(self):
        """Prune all expired tokens."""
        for token, expiry in self.tokens.items():
            if datetime.now(tz=timezone.utc) - expiry > timedelta(seconds=10):
                self.tokens.pop(token, None)
        for user_id, tokens in self.user_id_token_map.items():
            for token in tokens:
                if token not in self.tokens:
                    tokens.remove(token)
            if len(tokens) == 0:
                self.user_id_token_map.pop(user_id)

access_token_db = app.state.access_token_db = AccessTokenDB()

def generate_new_token(length: int=32) -> str:
    """Generate a new token.

    :return: The new token.
    """
    return secrets.token_urlsafe(length)

async def get_new_token(user: User | None = None, refresh_token: str | None = None) -> Tokens:
    """Get a new access token for a user.

    :param user: The user to get a new token for, if no refresh token is provided.
    :param refresh_token: The refresh token to get a new access token for.
    :return: The new access token and refresh token.
    """
    if refresh_token:
        refresh_token_obj = await UserTokens.objects.get_or_none(token=refresh_token)
        if not refresh_token_obj:
            raise HTTPException(status_code=401, detail="Invalid refresh token.")
        user_id = refresh_token_obj.user.id
        if datetime.now(tz=timezone.utc) - refresh_token_obj.expiry.astimezone(timezone.utc) < timedelta(minutes=5):
            raise HTTPException(status_code=401, detail="Expired refresh token.")
        new_token = generate_new_token()
        access_token_db.add_token(new_token, user_id)
        return Tokens(access_token=new_token, refresh_token=refresh_token)
    else:
        if not user:
            raise ValueError("No user provided.")
        user_id = user.id
        new_token = generate_new_token()
        new_refresh_token = generate_new_token(length=64)
        access_token_db.add_token(new_token, user_id)
        await UserTokens.objects.create(user=user, token=new_refresh_token, expiry=datetime.now(tz=timezone.utc).replace(tzinfo=None) + timedelta(days=30))
        return Tokens(access_token=new_token, refresh_token=new_refresh_token)
    
async def get_user_or_401(authorization_header: str) -> User:
    """Get the user from the request, or raise a 401 if the user is not authenticated."""
    assert authorization_header.startswith("Bearer ")
    access_token = authorization_header[7:]
    if not access_token_db.token_valid(access_token):
        raise HTTPException(status_code=401, detail="Not authenticated.")
    user_id = access_token_db.token_to_user_id_map[access_token]
    return await get_user_from_user_id(user_id)
    
def validate_and_normalize_email(email: str) -> str:
    """Validate and normalize an email.

    :param email: The email to validate and normalize.
    :return: The normalized email.
    """
    try:
        valid_email = validate_email(email)
        email = valid_email.email
    except EmailNotValidError as e:
        raise HTTPException(status_code=400, detail="Invalid email address.")
    return email