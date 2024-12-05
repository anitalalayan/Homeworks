import aiofiles
import asyncio
import json
from errors import *


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