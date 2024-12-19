"""
This module handles user authentication and registration functionalities.
"""
from passlib.context import CryptContext
from utils.helpers import read_db, write_to_db
from models.schemas import User


pwd_context: CryptContext = CryptContext(schemes=["sha256_crypt"])



def register_user(user: User) -> bool:
    """
    Register a new user in the database.
    """
    db = read_db("users.json")
    if user.username in db:
        return False

    hashed_password = pwd_context.hash(user.password)
    db[user.username] = {"username": user.username, "password": hashed_password, "email": user.email}
    write_to_db("users.json",db)
    return True

def authenticate_user(user: User) -> bool:
    """
        Authenticate a user based on the provided credentials.
    """
    users = read_db("users.json")
    current_user = users.get(user.username)
    if not current_user:
        return False
    return pwd_context.verify(user.password, current_user["password"])
