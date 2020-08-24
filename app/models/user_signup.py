from pydantic import BaseModel
from typing import Optional

class UserSignup(BaseModel):
    email: str
    username: str
    password: str
