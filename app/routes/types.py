from app.db import Mongo
from bson.objectid import ObjectId
from fastapi import APIRouter, Form

from ..models.type import Type

db = Mongo()
types_collection = db.types

router = APIRouter()


@router.get('')
async def get_types():
    types = await Type.get_all()
    return {'types': types}


@router.post('/create_type')
async def create_type(type: str = Form(...)):
    doc = {'type': type}
    await types_collection.insert_one(doc)

    return {'success': True}
