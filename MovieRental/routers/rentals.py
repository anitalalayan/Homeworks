"""
Rentals-related routes for the MovieRental application.

"""
from fastapi import APIRouter, HTTPException, Depends
from utils.helpers import  get_rentals, get_movies, update_rentals
from utils.auth_utils import verify_jwt_token

from models.schemas import Rental


rentals_router = APIRouter()

@rentals_router.get("/rentals")
async def get_all_rentals(username=Depends(verify_jwt_token)):
    """
    Retrieves the list of rentals for the currently logged-in user.
    """
    rentals = get_rentals()
    user_rentals = [rental for rental in rentals.values() if rental['user'] == username]
    return {"rentals": user_rentals }

@rentals_router.post("/rentals")
async def create_rental(rental: Rental, username=Depends(verify_jwt_token)):
    """    Creates a new rental entry for the currently logged-in user.
    """
    rentals = get_rentals()
    movies = get_movies()

    if rental.movie not in movies:
        raise HTTPException(status_code=404, detail="Movie not found")

    rental_data = rental.dict()
    rental_data["user"] = username
    rentals[rental.user] = rental_data
    update_rentals(rentals)

