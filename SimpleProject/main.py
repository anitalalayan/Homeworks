from fastapi import FastAPI, HTTPException
import aiofiles
import asyncio
import json
import os
from dotenv import load_dotenv
from errors import *

USERS_FILE = os.getenv("USERS_FILE", "users.json")
TASKS_FILE = os.getenv("TASKS_FILE", "tasks.json")
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))


app = FastAPI()


async def initialize_file(file_path: str):
    """ Initialising and populating the file if it doesn't exist """
    try:
        async with aiofiles.open(file_path, mode='w') as f:
            await f.write(json.dumps([]))
    except Exception as e:
        raise FileError(f"Error initializing {file_path}: {str(e)}")


async def read_from_file(file_path: str):

    """ Read the files asynchronously"""

    try:
        async with aiofiles.open(file_path, mode='r') as f:
            content = await f.read()
            return json.loads(content)
    except FileError:
        await initialize_file(file_path)
        return []
    except json.JSONDecodeError:
        raise FileError(f"File {file_path} contains invalid JSON.")

    except Exception as e:
        raise FileError(f" Unexpected error occurred reading {file_path}: {str(e)}")


async def write_to_file(file_path: str, content: dict):

    """ Write to the files asynchronously"""
    try:
        async with aiofiles.open(file_path, mode='w') as f:
            await f.write(json.dumps(content, indent=2))

    except Exception as e:
        raise FileError(f"Error writing {file_path}: {content}")




@app.get('/users')
async def get_users()-> list:
    """ Fetch and return all users """

    users = await read_from_file('users.json')
    return users

@app.get('/users/{user_id}')
async def get_user(user_id:int) -> dict:
    """ Fetch and return a single user by 'id'"""

    users = await read_from_file('users.json')
    user = next((u for u in users if u['id'] == user_id), None)
    if user is None:
        raise NotFoundError(f"User {user_id} not found")
    return user


@app.post('/users')
async def create_user(user:dict):
    """ Create a new user """

    if not isinstance (user['name'], str) or not user['name'].strip():
        raise ValidationError('Name must be a non-empty string')

    if not '@' in user['email'] or  user['email'].split('@')[0].startswith('.') or user['email'].endswith('.'):
        raise ValidationError('Invalid email address')

    if  len(user["password"]) < 6:
        raise ValidationError("Password must be at least 6 characters long.")


    users = await read_from_file('users.json')

    user['id'] = max((u.get('id', 0) for u in users), default=0) + 1

    users.append(user)

    await write_to_file('users.json', users)
    return {"message": "User created successfully", "users": users}



@app.put('/users/{user_id}')
async def update_user(user_id:int, data:dict) -> dict:
    """ Update a single user by id """
    users = await read_from_file('users.json')
    for user in users:
        if user['id'] == user_id:
            for key, value in data.items():
                if key in user:
                    user[key] = value
            await write_to_file('users.json', users)
            return {"message": "User updated successfully", "user": user}
    raise NotFoundError("User does not exist")



@app.delete('/users/{user_id}')
async def delete_user(user_id:int) -> dict:
    """ Delete a single user by id """

    users = await read_from_file('users.json')
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            await write_to_file('users.json', users)
            return {"message": "User deleted successfully", "user": user}
    raise NotFoundError("User not found")



@app.get('/tasks')
async def get_tasks()-> list:
    """ Fetch and return all tasks """

    tasks = await read_from_file('tasks.json')
    return tasks



@app.get('/tasks/{task_id}')
async def get_task(task_id: int) -> dict:
    """ Fetch and return a single task by id """

    tasks = await read_from_file('tasks.json')
    for task in tasks:
        if task['user_id'] == task_id:
            return task
    raise NotFoundError("Task not found")


@app.post('/tasks')
async def create_task(task:dict):
    """ Create a new task """

    users = await read_from_file('users.json')

    if not isinstance (task['title'], str) or not task['title'].strip():
        raise ValidationError('Title must be a non-empty string')
    if 'description' in task and not isinstance(task['description'], str):
        raise ValidationError('Description must be string if provided')

    user_exists = next((True for user in users if user['id'] == task['user_id']), False)
    if user_exists == False:
        raise NotFoundError('User not found')


    tasks = await read_from_file('tasks.json')
    tasks.append(task)
    await write_to_file('tasks.json', tasks)
    return {"message": "Task created successfully", "tasks": tasks}



@app.put('/tasks/{task_id}')
async def update_task(task_id: int, data:dict) -> dict:
    """ Update a single task by id """

    users = await read_from_file('users.json')

    if not isinstance (data['title'], str) or not data['title'].strip():
        raise ValidationError('Title must be a non-empty string')
    if 'description' in data and not isinstance(data['description'], str):
        raise ValidationError('Description must be string if provided')

    user_exists = next((True for user in users if user['id'] == data['user_id']), False)
    if user_exists == False:
        raise NotFoundError('User not found')

    tasks = await read_from_file('tasks.json')
    for task in tasks:
        if task['user_id'] == task_id:
            for key, value in data.items():
                if key in task:
                    task[key] = value
                    await write_to_file('tasks.json', tasks)
                    return {"message": "Task updated successfully", "task": task}
    raise NotFoundError("Task not found")




@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int) -> dict:
    """ Delete a single task by id """

    tasks = await read_from_file('tasks.json')
    for task in tasks:
        if task['user_id'] == task_id:
            tasks.remove(task)
            await write_to_file('tasks.json', tasks)
            return {"message": "Task deleted successfully"}
    raise NotFoundError("Task not found")

@app.post('/register')
async def register_user(user:dict) -> dict:
    """ Register a new user """

    if not isinstance (user['name'], str) or not user['name'].strip():
        raise ValidationError('Name must be a non-empty string')
    if not '@' in user['email'] or user['email'].endswith('.'):
        raise ValidationError('Invalid email address')
    if len(user['password']) < 6:
        raise ValidationError('Password must be at least 6 characters long.')

    users = await read_from_file('users.json')
    user['id'] = max((u.get('id', 0) for u in users), default=0) + 1
    users.append(user)
    await write_to_file('users.json', users)
    return {"message": "User registered successfully", "user": user}


@app.post('/login')
async def login_user(user:dict) -> dict:
    """ Login a user """

    existing_users = await read_from_file('users.json')
    for existing_user in existing_users:
        if existing_user['email'] == user['email'] and existing_user['password'] == user['password']:
            return {"message": "User logged successfully", "user": existing_user}

    raise ValidationError("Invalid email or password")



if __name__ == '__main__':
    uvicorn.run(app, host=HOST, port=PORT, reload=True)





