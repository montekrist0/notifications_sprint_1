from functools import lru_cache

from core.configs import settings
from services.base import BaseEventService


class PersonalSelectionService(BaseEventService):
    pass


@lru_cache(maxsize=None)
def get_personal_selection_service():
    return PersonalSelectionService(settings.rabbitmq_queue_send_personal_selection)
