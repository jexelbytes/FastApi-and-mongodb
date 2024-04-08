from fastapi import HTTPException

class UserNotFoundException(Exception):
    def __init__(self):
        raise HTTPException(status_code=404,detail="User record not found!")