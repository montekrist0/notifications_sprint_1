from functools import lru_cache

from core.configs import settings
from services.base import BaseEventService


class BulkEventService(BaseEventService):
    pass


@lru_cache(maxsize=None)
def get_bulk_event_service():
    return BulkEventService(settings.rabbitmq_queue_send_bulk_mails)
