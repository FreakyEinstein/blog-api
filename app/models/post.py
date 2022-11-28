from app.db import Mongo
from pydantic import BaseModel, validator
from fastapi import HTTPException

from .type import Type

db = Mongo()
posts_collection = db.posts
types_collection = db.types


class Post(BaseModel):
    postType: str = None
    title: str
    content: str

    @validator('postType')
    async def validate_type(cls, postType):
        types = []
        async for type in types_collection.find():
            types.append(type['type'])
        if postType not in types:
            raise ValueError("Type not Available")
        else:
            return postType

    async def save(doc):
        doc = {k: v for k, v in doc.items() if v is not None}
        try:
            doc['postType'] = await Post.validate_type(doc['postType'])
        except Exception as e:
            raise HTTPException(status_code=501, detail=f"{str(e)}")

        await posts_collection.insert_one(doc)

        return True
