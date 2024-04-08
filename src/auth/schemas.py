from beanie import Document
from beanie import PydanticObjectId
from datetime import datetime
from pydantic import BaseModel, model_validator
from .extra import hash_password
from pydantic import EmailStr, Field

class ActiveSession(Document):
    
    user_id: PydanticObjectId
    token: str = None
    expire_at: datetime
    created_at: datetime = datetime.now()
    
class LoginCreds(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=512)
    
    @model_validator(mode="after")
    def validate_email(self ) -> 'LoginCreds':
        self.password = hash_password(self.password)
        self.email = self.email.lower()
        return self