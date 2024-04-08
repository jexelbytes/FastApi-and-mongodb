import uvicorn
from config import API_HOST, API_PORT, IS_DEV

if __name__ == "__main__":
    uvicorn.run("app:app", host=API_HOST, port=API_PORT, reload=IS_DEV)