from functools import lru_cache

from core.configs import settings
from db.clients.mongo import get_mongo_client
from motor.motor_asyncio import AsyncIOMotorCollection
from services.service_models import UserInfo


class UserPreferenceService:
    def __init__(self, mongo_collection_of_users: AsyncIOMotorCollection):
        self.mongo_collection_of_users = mongo_collection_of_users

    async def get_user_info(self, user_id: str):
        user_info_doc = await self.mongo_collection_of_users.find_one(
            {"user_id": user_id}
        )
        return UserInfo.parse_obj(user_info_doc)

    async def set_user_preference(self, user_id: str, preference: dict):
        result = await self.mongo_collection_of_users.update_one(
            {"user_id": user_id}, {"$set": preference}
        )
        if result.modified_count:
            return True


@lru_cache(maxsize=None)
def get_user_pref_service():
    client = get_mongo_client()
    db = client[settings.mongo_db]
    collection = db[settings.user_preference_collection]
    return UserPreferenceService(collection)