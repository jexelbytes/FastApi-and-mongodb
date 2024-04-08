from pydantic import BaseModel, model_validator
from typing import Optional
from pydantic import AnyUrl, EmailStr, Field
from auth.extra import hash_password
from .documents import User

class CreateUser(BaseModel):
    
    email: EmailStr
    first_name: str = Field(min_length=1, max_length=128)
    last_name: str = Field(min_length=1, max_length=128)
    age: Optional[int] = Field(ge=18, default=None)
    password: str = Field(min_length=8, max_length=512)
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
    
    @model_validator(mode="after")
    def validate_pass(self ) -> 'UpdateUser':
        self.password = hash_password(self.password)
        return self
    
    @model_validator(mode="after")
    def validate_email(self) -> 'CreateUser':
        self.email = self.email.lower()
        user = User.find_one({"email":self.email})
        if user:
            raise ValueError("email already in use.")
        
        return self

class UpdateUser(BaseModel):
    
    email: EmailStr = None
    first_name: str = Field(min_length=1, max_length=128, default=None)
    last_name: str = Field(min_length=1, max_length=128, default=None)
    age: int = Field(ge=18, default=None)
    password: Optional[str] = Field(min_length=8, max_length=512, default=None)
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
    
    @model_validator(mode="after")
    def validate_pass_email(self ) -> 'UpdateUser':
        
        if self.password != None:
            self.password = hash_password(self.password)
        
        if self.email != None:
            self.email = self.email.lower()
        
        return self