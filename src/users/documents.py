
from beanie import Document, Indexed
from pydantic import model_serializer
from typing import Optional, Any, Annotated, Dict
from pydantic import AnyUrl, EmailStr, Field

class User(Document):
    
    email: Annotated[EmailStr, Indexed(unique=True)]
    first_name: str = Field(min_length=1, max_length=128)
    last_name: str = Field(min_length=1, max_length=128)
    age: Optional[int] = Field(ge=18, default=None)
    password: str = Field(min_length=8, max_length=512)
    photo: AnyUrl = None
    
    @model_serializer
    def serialized_model(self) -> Dict[str, Any]:
        return {
            "id": str(self.id),
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "photo": self.photo
        }
