from fastapi import FastAPI, HTTPException
import uvicorn
import os
from models import User, Task
from utilities import read_from_file, write_to_file, initialize_file
from errors import *

from dotenv import load_dotenv

load_dotenv()


USERS_FILE = os.getenv("USERS_FILE", "users.json")
TASKS_FILE = os.getenv("TASKS_FILE", "tasks.json")
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))


app = FastAPI()


@app.get('/users')
async def get_users()-> list:
    """ Fetch and return all users """

    users = await read_from_file(USERS_FILE)
    return users

@app.get('/users/{user_id}')
async def get_user(user_id:int) -> dict:
    """ Fetch and return a single user by 'id'"""

    users = await read_from_file(USERS_FILE)
    user = next((u for u in users if u['id'] == user_id), None)
    if user is None:
        raise NotFoundError(f"User {user_id} not found")
    return user


@app.post('/users')
async def create_user(user: User)-> list:
    """ Create a new user """

    users = await read_from_file(USERS_FILE)
    user['id'] = max((u.get('id', 0) for u in users), default=0) + 1
    users.append(user)

    await write_to_file(USERS_FILE, users)
    return {"message": "User created successfully", "users": users}



@app.put('/users/{user_id}')
async def update_user(user_id:int, data: User) -> dict:
    """ Update a single user by id """
    users = await read_from_file(USERS_FILE)
    for user in users:
        if user['id'] == user_id:
            for key, value in data.items():
                if key in user:
                    user[key] = value
            await write_to_file(USERS_FILE, users)
            return {"message": "User updated successfully", "user": user}
    raise NotFoundError("User does not exist")



@app.delete('/users/{user_id}')
async def delete_user(user_id:int) -> dict:
    """ Delete a single user by id """

    users = await read_from_file(USERS_FILE)
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            await write_to_file(USERS_FILE, users)
            return {"message": "User deleted successfully", "user": user}
    raise NotFoundError("User not found")



@app.get('/tasks')
async def get_tasks()-> list:
    """ Fetch and return all tasks """

    tasks = await read_from_file(TASKS_FILE)
    return tasks



@app.get('/tasks/{task_id}')
async def get_task(task_id: int) -> dict:
    """ Fetch and return a single task by id """

    tasks = await read_from_file(TASKS_FILE)
    for task in tasks:
        if task['user_id'] == task_id:
            return task
    raise NotFoundError("Task not found")


@app.post('/tasks')
async def create_task(task: Task)->list:
    """ Create a new task """

    users = await read_from_file(USERS_FILE)
    user_exists = next((True for user in users if user['id'] == task['user_id']), False)
    if not user_exists:
        raise NotFoundError('User not found')


    tasks = await read_from_file(TASKS_FILE)
    tasks.append(task)
    await write_to_file(TASKS_FILE, tasks)
    return {"message": "Task created successfully", "tasks": tasks}



@app.put('/tasks/{task_id}')
async def update_task(task_id: int, data: Task) -> dict:
    """ Update a single task by id """

    users = await read_from_file(USERS_FILE)
    user_exists = next((True for user in users if user['id'] == data['user_id']), False)
    if not user_exists:
        raise NotFoundError('User not found')

    tasks = await read_from_file(TASKS_FILE)
    for task in tasks:
        if task['user_id'] == task_id:
            for key, value in data.items():
                if key in task:
                    task[key] = value
                    await write_to_file(TASKS_FILE, tasks)
                    return {"message": "Task updated successfully", "task": task}
    raise NotFoundError("Task not found")




@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int) -> dict:
    """ Delete a single task by id """

    tasks = await read_from_file(TASKS_FILE)
    for task in tasks:
        if task['user_id'] == task_id:
            tasks.remove(task)
            await write_to_file(TASKS_FILE, tasks)
            return {"message": "Task deleted successfully"}
    raise NotFoundError("Task not found")

@app.post('/register')
async def register_user(user: User) -> dict:
    """ Register a new user """

    users = await read_from_file(USERS_FILE)
    user['id'] = max((u.get('id', 0) for u in users), default=0) + 1
    users.append(user)
    await write_to_file(USERS_FILE, users)
    return {"message": "User registered successfully", "user": user}


@app.post('/login')
async def login_user(user:User) -> dict:
    """ Login a user """

    existing_users = await read_from_file(USERS_FILE)
    for existing_user in existing_users:
        if existing_user['email'] == user['email'] and existing_user['password'] == user['password']:
            return {"message": "User logged successfully", "user": existing_user}

    raise ValidationError("Invalid email or password")



if __name__ == '__main__':
    uvicorn.run('main:app', host=HOST, port=PORT, reload=True)





