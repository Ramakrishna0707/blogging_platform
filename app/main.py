from fastapi import FastAPI
from app.routers import post, comment  # Ensure correct import path

app = FastAPI()

app.include_router(post.router, prefix="/posts", tags=["posts"])
app.include_router(comment.router, prefix="/comments", tags=["comments"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Blogging Platform API"}
