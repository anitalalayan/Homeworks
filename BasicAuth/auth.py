"""
This module contains the authentication logic for user login, logout, and session management.
"""
from users_db import get_users_db
from users_db import verify_password

sessions: set[str] = set()

def authenticate_user(username: str, password: str) -> bool:
    """
    Authenticate the user by checking their username and password.
    """
    db = get_users_db()
    user = db.get(username)
    if not user:
        return False
    authenticated = verify_password(password, user["password"])
    if authenticated:
        sessions.add(username)
    return authenticated


def is_authenticated(username: str) -> bool:
    """
    Check if the user is authenticated (i.e., if their session exists).
    """
    return username in sessions

def terminate_session(username: str) -> bool:
    """ Terminate a session. """
    if is_authenticated(username):
        sessions.remove(username)
        return True
    return False
