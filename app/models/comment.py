from pydantic import BaseModel, Field
from bson import ObjectId

class Comment(BaseModel):
    id: str = Field(default_factory=ObjectId, alias="_id")
    post_id: str
    content: str

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str,
        }