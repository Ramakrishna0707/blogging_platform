import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_post():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/posts/", json={"title": "Test Post", "content": "Content of the test post"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Post"

@pytest.mark.asyncio
async def test_get_post():
    post_id = "some_post_id"
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id
