import os
from dotenv import load_dotenv
load_dotenv()

# DATABASE CREDENTIALS
DATABASE_URI = os.getenv("DATABASE_URI")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_RETRY_WRITES = "true" if os.getenv("DATABASE_RETRY_WRITES").lower() in ("true", "1") else "false"

# JWT
JWT_SECRET = os.getenv('JWT_SECRET')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
JWT_EXPIRE_TIME = float(float(os.getenv('JWT_EXPIRE_TIME'))*3600.0)
JWT_REFRESH_EXPIRE_TIME = float(float(os.getenv('JWT_REFRESH_EXPIRE_TIME'))*3600.0)

# API CONFIGURATION
API_HOST = os.getenv("API_HOST")
API_PORT = int(os.getenv("API_PORT"))
IS_DEV = str(os.getenv("IS_DEV")).lower() in ("true", "1")
SHOW_SWAGGER = str(os.getenv("SHOW_SWAGGER")).lower() in ("true", "1")
MAINTAINER_USERNAME = str(os.getenv('MAINTAINER_USERNAME'))
MAINTAINER_PASSWORD = str(os.getenv('MAINTAINER_PASSWORD'))

description = """ ### Description:
This project consists of an API created with the intention of learning good practices in the implemented technologies."""

app_configs = {
    "title":os.getenv("TITLE"),
    "summary":"FastAPI / MongoDB learnig API.",
    "description":description,
    "docs_url":None,
    "redoc_url":None,
    "openapi_url":None,
}

swagger_config = {
    "syntaxHighlight.theme": "nord",
    "persistAuthorization": True,
    "tryItOutEnabled":True,
    "docExpansion": "none",
    "displayRequestDuration":True,
    "filter":True,
}