from functools import lru_cache

import pymongo
from core.config import settings


@lru_cache()
def get_mongo_worker_client():
    mongo_worker_client = pymongo.MongoClient(
        host=settings.worker_mongo_host, port=settings.worker_mongo_port, maxPoolSize=10
    )
    return mongo_worker_client
