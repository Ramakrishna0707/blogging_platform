from pydantic import BaseModel, Field
from typing import List
from bson import ObjectId

class Post(BaseModel):
    id: str = Field(default_factory=ObjectId, alias="_id")
    title: str
    content: str
    likes: int = 0
    dislikes: int = 0
    comments: List[str] = []

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str,
        }
