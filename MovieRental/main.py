"""
This module initializes the FastAPI app and includes the routers for
authentication, movie management, and rentals.
"""
import os
from fastapi import  FastAPI
import uvicorn
from dotenv import load_dotenv

from routers.auth import auth_router
from routers.movies import movies_router
from routers.rentals import rentals_router

load_dotenv()
PORT = os.getenv('PORT')

app = FastAPI()

app.include_router(auth_router)
app.include_router(movies_router)
app.include_router(rentals_router)

@app.get("/")
async def root():
    """
     A welcome message.
    """
    return "Welcome to MovieRental!"

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(PORT), reload=True)

