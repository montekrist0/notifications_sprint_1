import typing

import motor.motor_asyncio
from core.configs import settings
from motor.motor_asyncio import AsyncIOMotorCollection

host = settings.mongo_user_preference_host
port = settings.mongo_user_preference_port

client: typing.Union[AsyncIOMotorCollection, None] = None


def create_mongo_client():
    return motor.motor_asyncio.AsyncIOMotorClient(host=host, port=port, maxPoolSize=10)


def get_mongo_client():
    return client
