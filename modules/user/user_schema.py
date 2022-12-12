from typing import Union, Literal

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class UserCreate(BaseModel):
    username: str
    email: Union[str, None] = None


class User(UserCreate):
    id: str
    role: Literal["admin", "team_user"]


class UserInDB(User):
    hashed_password: str
