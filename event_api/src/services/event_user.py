from functools import lru_cache

from core.configs import settings
from services.base import BaseEventService


class EventUserService(BaseEventService):
    pass


@lru_cache(maxsize=None)
def get_event_user_service():
    return EventUserService(settings.rabbitmq_queue_send_mail)
