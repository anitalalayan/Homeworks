"""
Authentication routes for the MovieRental application.
"""

from fastapi import APIRouter, FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from models.schemas import User
from utils.auth_utils import create_jwt_token
from utils.db_utils import register_user, authenticate_user



auth_router = APIRouter()

@auth_router.post("/register")
async def register(user: User):
    """
       Checks if the user already exists and raises an error if so. Otherwise, creates a new user
       in the database and returns a success message.
       """
    if not register_user(user):
        raise HTTPException(detail="User already exists", status_code=status.HTTP_409_CONFLICT)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "User registered" })

@auth_router.post("/login")
async def login(user: User):
    """
    Checks if the provided credentials are valid and, if so, generates a JWT token.
    Returns the token to the user for subsequent requests.
    """
    if not authenticate_user(user):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    auth_token = create_jwt_token({"username": user.username})

    return JSONResponse(status_code=status.HTTP_200_OK,content={"message": "Logged in successfully", "auth_token": auth_token})