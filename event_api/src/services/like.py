from functools import lru_cache

from core.configs import settings
from services.base import BaseService


class LikeService(BaseService):
    pass


@lru_cache(maxsize=None)
def get_like_service():
    return LikeService(settings.rabbitmq_queue_send_like)
