from functools import lru_cache

import motor.motor_asyncio
from config import settings


@lru_cache()
def get_mongo_worker_client():
    mongo_worker_client = motor.motor_asyncio.AsyncIOMotorClient(
        host=settings.mongo_host, port=settings.mongo_port, maxPoolSize=10
    )
    return mongo_worker_client
