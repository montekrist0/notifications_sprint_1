from functools import lru_cache

from core.configs import settings
from services.base import BaseEventService


class WelcomeService(BaseEventService):
    pass


@lru_cache(maxsize=None)
def get_welcome_service():
    return WelcomeService(settings.rabbitmq_queue_send_welcome)
