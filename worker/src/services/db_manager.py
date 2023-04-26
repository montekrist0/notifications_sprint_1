import bson

from functools import lru_cache

from pymongo.database import Database
from pymongo.collection import Collection

from core.db import get_mongo_worker_client
from core.config import settings


class MongoDbManager:
    def __init__(self, mongo_db: Database):
        self.mongo_client: Database = mongo_db

    def insert_one(self, collection_name: str, data: dict):
        collection: Collection = self.mongo_client[collection_name]
        result = collection.insert_one(data)
        inserted_id = result.inserted_id
        if inserted_id:
            return inserted_id
        return None

    def update_status_by_id(self, collection_name: str, id_: str, status: int):
        collection: Collection = self.mongo_client[collection_name]
        filter_ = {"_id": bson.ObjectId(id_)}
        update = {"$set": {"status_id": status}}
        result = collection.update_one(filter_, update)


@lru_cache()
def get_db_manager():
    mongo_client = get_mongo_worker_client()
    mongo_db = mongo_client[settings.worker_mongo_db]
    return MongoDbManager(mongo_db)
