from fastapi import APIRouter, HTTPException
from models.comment import Comment
from schemas.comment import CommentCreate, CommentResponse
from database import db

router = APIRouter()

@router.post("/", response_model=CommentResponse)
async def create_comment(comment: CommentCreate):
    comment_data = comment.dict()
    result = await db["comments"].insert_one(comment_data)
    new_comment = await db["comments"].find_one({"_id": result.inserted_id})
    return new_comment

@router.get("/{comment_id}", response_model=CommentResponse)
async def get_comment(comment_id: str):
    comment = await db["comments"].find_one({"_id": comment_id})
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

@router.delete("/{comment_id}")
async def delete_comment(comment_id: str):
    delete_result = await db["comments"].delete_one({"_id": comment_id})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Comment deleted successfully"}
