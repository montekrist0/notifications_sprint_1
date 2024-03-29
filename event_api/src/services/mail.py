from functools import lru_cache

from core.configs import settings
from services.base import BaseEventService


class MailService(BaseEventService):
    pass


@lru_cache(maxsize=None)
def get_mail_service():
    return MailService(settings.rabbitmq_queue_send_mail)
