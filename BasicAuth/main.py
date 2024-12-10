"""
This is the main application entry point for the FastAPI-based web app.
It handles user registration, login, and access to a secure page for authenticated users.
"""

import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request, Form, status, Response, Cookie, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn

from auth import authenticate_user, is_authenticated, terminate_session
from users_db import register_user
from logs import Logs

load_dotenv()

PORT: int = int(os.environ.get('PORT'))

templates: Jinja2Templates = Jinja2Templates(directory="templates")

logger = Logs()

app: FastAPI = FastAPI()


def get_current_username(username: str = Cookie(None)) -> str:
    """
    Get the current username from the cookie.
    """
    if not username:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return username



@app.get("/login", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    """
    Render the login page.
    """
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def login_user(response: Response, username: str = Form(...), password: str = Form(...)):
    """
        Handle the user login.
    """
    if not authenticate_user(username, password):
        logger.log("login", username=username, status= "Failed")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    logger.log("login", username=username, status="Success")
    redirect_response = RedirectResponse(url='/secure', status_code=status.HTTP_303_SEE_OTHER)
    redirect_response.set_cookie(key="username", value=username)
    return redirect_response



@app.get("/register", response_class=HTMLResponse)
async def register(request: Request) -> HTMLResponse:
    """
    Render the registration page.
    """
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/register")
async def register_user_form(username: str = Form(...), password: str = Form(...)):
    """
    Handle the user registration form submission.
    """
    if not register_user(username, password):
        logger.log("register", username=username, status= "Failed")
        raise HTTPException(status_code=400, detail="Username already exists")
    logger.log("register", username=username, status="Success")
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/secure")
async def secure_page(request: Request, username: str = Depends(get_current_username)):
    """
    Render the secure page only if the user is authenticated.
    """
    if not is_authenticated(username):
        logger.log("secure", username=username, status= "Failed")
        return RedirectResponse("/login", status_code=status.HTTP_303_SEE_OTHER)
    logger.log("secure_page_access", username=username, status="Success")
    return templates.TemplateResponse("secure.html", {"request": request, "username": username})



@app.get("/logout")
def logout_user(response: Response, username: str = Depends(get_current_username)):
    """
    Log out the user by removing their session and deleting the cookie.
    """
    if terminate_session(username):
        logger.log("logout", username=username, status= "Success")
        response.delete_cookie('username')
    return RedirectResponse(url='/login', status_code=status.HTTP_303_SEE_OTHER)



if __name__ == '__main__':
    uvicorn.run("main:app", port=PORT, reload=True)
