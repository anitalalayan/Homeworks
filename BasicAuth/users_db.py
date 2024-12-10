"""
This module contains functions related to reading from and writing to the user database,
which is stored in a JSON file (`users.json`). It includes methods to register a user,
verify their password, and check if a username exists.
"""
import json
from passlib.context import CryptContext

USER_FILE: str = "users.json"

pwd_context: CryptContext = CryptContext(schemes=["sha256_crypt"])

def _initialize_user_file(users: dict) -> None:
    """
    Initialize the user file by saving the provided users dictionary to the JSON file.
    """
    try:
        with open(USER_FILE, 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=2)
    except Exception as e:
        print(f"Error initializing user file: {e}")


def _read_users_db() -> dict:
    """
    Read the users database from the JSON file.
    """
    try:
        with open(USER_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def get_users_db() -> dict:
    """Public method to access user data."""
    return _read_users_db()


def hash_password(password: str) -> str:
    """
    Hash the password using the CryptContext.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify if the plain password matches the hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)


def register_user(username: str, password: str) -> bool:
    """
    Register a new user by adding their username and hashed password to the database.
    """
    db = _read_users_db()
    if username in db:
        return False
    db[username] = {"username": username, "password": hash_password(password)}
    _initialize_user_file(db)
    return True
