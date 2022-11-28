from app.db import Mongo
from bson.objectid import ObjectId
from fastapi import APIRouter, Form

from ..models.post import Post

db = Mongo()
posts_collection = db.posts

router = APIRouter()


@router.get('')
async def get_all_posts():
    posts = []
    async for post in posts_collection.find():
        post['_id'] = str(post['_id'])
        posts.append(post)

    return {'posts': posts}


@router.post('')
async def create_post(
    postType: str = Form(...),
    title: str = Form(...),
    content: str = Form(...)
):
    doc = {'postType': postType.lower(), 'title': title, 'content': content}
    success = await Post.save(doc)
    return {'success': success}
