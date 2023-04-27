from functools import lru_cache

import bson
from core.config import settings
from core.db import get_mongo_worker_client
from pymongo.collection import Collection
from pymongo.database import Database


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
        collection.update_one(filter_, update)

    def update_like_by_id(self, collection_name: str, id_: bson.ObjectId):
        collection: Collection = self.mongo_client[collection_name]
        filter_ = {"_id": id_}
        update = {"$inc": {"content.likes_count_new": 1}}
        collection.update_one(filter_, update)

    def check_like(self, collection_name: str, user_id: str, review_id: int):
        collection: Collection = self.mongo_client[collection_name]
        filter_ = {"content.user_id": user_id, "content.review_id": review_id}
        result = collection.find_one(filter=filter_)
        return result


@lru_cache()
def get_db_manager():
    mongo_client = get_mongo_worker_client()
    mongo_db = mongo_client[settings.worker_mongo_db]
    return MongoDbManager(mongo_db)
