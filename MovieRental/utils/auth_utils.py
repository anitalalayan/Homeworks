"""
Module for handling JWT authentication in the FastAPI application.
"""
import os
import datetime
from dotenv import load_dotenv
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status


load_dotenv()

ALGORITHM = "HS256"
EXPIRES_IN = 600
SECRET_KEY = os.getenv('JWT_SECRET_KEY')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")



def create_jwt_token(user:dict):
  """
  Create JWT token
  """
  expires = datetime.datetime.utcnow() + datetime.timedelta(seconds=EXPIRES_IN)
  data = user.copy()
  data['exp'] = expires
  data['username'] = user["username"]

  auth_token = jwt.encode(data,SECRET_KEY, algorithm=ALGORITHM)
  print(auth_token)
  return auth_token


def verify_jwt_token(token:str = Depends(oauth2_scheme)):
  """
  Verify the validity of a JWT token and extract the username from it.
  """
  print(f"Received token: {token}")
  try:

    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    print(f"Decoded payload: {payload}")

    username = payload.get("username")
    return username

  except JWTError as exc:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from exc