from functools import lru_cache

import orjson
from aiormq.abc import DeliveredMessage
from core.config import settings
from services.context import (
    ContextUsersCollectService,
    get_context_user_service,
)
from services.notification import (
    NotificationEmailService,
    get_notification_email_service)


class EventHandler:
    def __init__(
            self,
            notification_email: NotificationEmailService,
            context_user_service: ContextUsersCollectService,
    ):
        self.notification_email = notification_email
        self.user_service = context_user_service

    async def handler_event_welcome(self, message: DeliveredMessage):
        content: dict = orjson.loads(message.body)

        user_id: str = content['user_id']
        user = await self.user_service.get_user(user_id)
        if user:
            await self.notification_email.send_notification('1', content, user,
                                                            settings.worker_mongo_collection_notifications)

    async def handler_event_personal_selection(self, message: DeliveredMessage):
        message_body = orjson.loads(message.body)
        for content in message_body:
            user_id = content['user_id']
            user = await self.user_service.get_user(user_id)
            if user:
                await self.notification_email.send_notification('3', message_body, user,
                                                                settings.worker_mongo_collection_notifications)

    async def handler_event_bulk_mails(self, message: DeliveredMessage):
        message_body = orjson.loads(message.body)
        group_id = message_body['group_id']
        users = await self.user_service.get_users(group_id=group_id)
        if users:
            for user in users:
                await self.notification_email.send_notification('4', message_body['content'], user,
                                                                settings.worker_mongo_collection_notifications)

    async def handler_event_mail(self, message: DeliveredMessage):
        message_body = orjson.loads(message.body)
        if 'user_id' in message_body:
            user_id: str = message_body['user_id']
            user = await self.user_service.get_user(user_id)
            if user:
                await self.notification_email.send_notification('5', message_body, user,
                                                                settings.worker_mongo_collection_notifications)
        else:
            await self.notification_email.send_notification('5', message_body, message_body,
                                                            settings.worker_mongo_collection_notifications)

    async def handler_event_like(self, message: DeliveredMessage):
        message_body = orjson.loads(message.body)
        await self.notification_email.update_or_create_notification_like(
            settings.worker_mongo_collection_notifications,
            message_body['user_id'],
            message_body['review_id'],
        )


@lru_cache(maxsize=None)
def get_event_handler_service():
    notification_email_service = get_notification_email_service()
    context_user_service = get_context_user_service()
    return EventHandler(
        notification_email=notification_email_service,
        context_user_service=context_user_service,
    )
