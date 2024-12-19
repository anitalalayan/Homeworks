"""
This module contains Pydantic models used for validation of user input.
"""
from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    """
    Represents a user in the system.
    """
    username: str = Field(..., min_length=3, max_length=30)
    password: str = Field(..., min_length=6, max_length=30)
    email: EmailStr


class Movie(BaseModel):
    """
        Represents a user in the system.
    """
    title: str = Field(..., min_length=3, max_length=30)
    genre: str = Field(..., min_length=3, max_length=30)
    rating: float = Field(..., ge=0, le=5)

class Rental(BaseModel):
    """
    Represents a user in the system.
    """
    user: str
    movie: str
    rental_duration: int = Field(..., ge=0, le=5)

