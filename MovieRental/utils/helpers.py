"""
This module contains utility functions for reading and writing data to JSON files.
"""
import os
import json
from json import JSONDecodeError


def write_to_db(file_path, data):
    """    Writes the provided data to a JSON file at the given file path.
    """
    try:
        with open(file_path, mode='w', encoding="utf-8") as file:
            json.dump(data, file, indent=2)
    except JSONDecodeError:
        return {}

def read_db(file_path)->dict:
    """ Reads the JSON file at the given file path."""
    if not os.path.exists(file_path):
        return {}
    try:
        with open(file_path,'r', encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}

USERS_FILE = "users.json"
MOVIES_FILE = "movies.json"
RENTALS_FILE = "rentals.json"

def get_users():
    """ Retrieves the list of users from the users file."""
    return read_db(USERS_FILE)

def update_users(users):
    """ Updates the list of users from the users file."""
    write_to_db(USERS_FILE, users)

def get_movies():
    """ Retrieves the list of movies from the movies file."""
    return read_db(MOVIES_FILE)

def update_movies(movies):
    """ Updates the list of movies from the movies file."""
    write_to_db(MOVIES_FILE, movies)

def get_rentals():
    """ Retrieves the list of rentals from the movies file."""
    return read_db(RENTALS_FILE)

def update_rentals(rentals):
    """ Updates the list of rentals from the movies file."""
    write_to_db(RENTALS_FILE, rentals)