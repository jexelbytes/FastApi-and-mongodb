from fastapi import HTTPException

class ExpiredRefreshException(Exception):
    def __init__(self):
        raise HTTPException(status_code=401, detail="Expired refresh.")

class ExpiredTokenException(Exception):
    def __init__(self):
        raise HTTPException(status_code=401, detail="Expired token.")

class InvalidTokenException(Exception):
    def __init__(self):
        raise HTTPException(status_code=401, detail="Invalid token.")