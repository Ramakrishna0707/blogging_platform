from fastapi import APIRouter, HTTPException, Depends
from models.post import Post
from schemas.post import PostCreate, PostUpdate, PostResponse
from database import db

router = APIRouter()

@router.post("/", response_model=PostResponse)
async def create_post(post: PostCreate):
    post_data = post.dict()
    result = await db["posts"].insert_one(post_data)
    new_post = await db["posts"].find_one({"_id": result.inserted_id})
    return new_post

@router.get("/{post_id}", response_model=PostResponse)
async def get_post(post_id: str):
    post = await db["posts"].find_one({"_id": post_id})
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/{post_id}", response_model=PostResponse)
async def update_post(post_id: str, post: PostUpdate):
    updated_post = await db["posts"].find_one_and_update(
        {"_id": post_id},
        {"$set": post.dict()},
        return_document=True
    )
    if updated_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post

@router.delete("/{post_id}")
async def delete_post(post_id: str):
    delete_result = await db["posts"].delete_one({"_id": post_id})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}
