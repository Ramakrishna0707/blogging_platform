from pydantic import BaseModel

class CommentCreate(BaseModel):
    post_id: str
    content: str

class CommentResponse(BaseModel):
    id: str
    post_id: str
    content: str
