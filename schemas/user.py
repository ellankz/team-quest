from typing import Union
from pydantic import BaseModel, SecretStr


class User(BaseModel):
    id: Union[str, None] = None
    email: str
    username: str
    password: SecretStr
