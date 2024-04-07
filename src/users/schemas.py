from beanie import Document
from pydantic import BaseModel
from typing import Optional
from typing_extensions import Annotated
from pydantic import AnyUrl, EmailStr, Field, constr

class User(Document):
    
    email: EmailStr
    first_name: str = Field(min_length=1, max_length=128)
    last_name: str = Field(min_length=1, max_length=128)
    age: Optional[int] = Field(ge=18, default=None)
    password: str
    photo: AnyUrl = None
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "email@email.com",
                    "first_name": "Iñigo",
                    "last_name": "Montoya",
                    "age": "18",
                    "password": "123",
                    "photo": "url"
                }
            ]
        }
    }
    
class UpdateUser(BaseModel):
    
    email: EmailStr = None
    first_name: str = Field(min_length=1, max_length=128, default=None)
    last_name: str = Field(min_length=1, max_length=128, default=None)
    age: int = Field(ge=18, default=None)
    password: str = None
    photo: AnyUrl = None
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "email@email.com",
                    "first_name": "Iñigo",
                    "last_name": "Montoya",
                    "age": "18",
                    "password": "123",
                    "photo": "url"
                }
            ]
        }
    }