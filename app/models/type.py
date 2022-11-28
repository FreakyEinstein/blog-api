from app.db import Mongo
from pydantic import BaseModel, validator

db = Mongo()
types_collection = db.types


class Type(BaseModel):
    type: str

    @classmethod
    async def get_all(self):
        types = []
        async for type in types_collection.find():
            type['_id'] = str(type['_id'])
            types.append(type)

        return types
