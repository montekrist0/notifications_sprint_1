from functools import lru_cache

from core.configs import settings
from services.base import BaseService


class BulkMailsService(BaseService):
    pass


@lru_cache(maxsize=None)
def get_bulk_mails_service():
    return BulkMailsService(settings.rabbitmq_queue_send_bulk_mails)
