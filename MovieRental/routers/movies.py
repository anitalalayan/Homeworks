"""
Movies-related routes for the MovieRental application.
"""
from fastapi import APIRouter, HTTPException, status
from models.schemas import Movie
from utils.helpers import update_movies,get_movies

movies_router = APIRouter()




@movies_router.get("/movies")
async def get_all_movies():
    """
    Retrieves a list of all available movies.
    """
    return {"movies": get_movies()}


@movies_router.post("/movies")
async def create_movie(movie: Movie):
    """
     Creates a new movie entry.
    """

    movies = get_movies()
    if movie.title in movies:
        raise HTTPException(detail="Movie already exists", status_code=status.HTTP_409_CONFLICT)
    movies[movie.title] = movie.dict()
    update_movies(movies)