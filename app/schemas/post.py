from pydantic import BaseModel
from typing import List

class PostCreate(BaseModel):
    title: str
    content: str

class PostUpdate(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    id: str
    title: str
    content: str
    likes: int
    dislikes: int
    comments: List[str]
