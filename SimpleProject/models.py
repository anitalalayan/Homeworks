from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional


class User(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=1)
    email: EmailStr
    password: str = Field(..., min_length=6)


class Task(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    user_id: int