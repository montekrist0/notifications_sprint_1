from functools import lru_cache

import orjson
from aiormq.abc import DeliveredMessage
from core.config import settings
from jinja2 import Template
from pymongo.database import Database
from services.context import (
    ContextTemplateCollectService,
    ContextUsersCollectService,
    get_context_template_service,
    get_context_user_service,
    )
from services.db_manager import get_db_manager
from services.tools import get_current_utc_datetime
from tasks import send_email


class EventHandler:
    def __init__(
        self,
        db_manager: Database,
        context_user_service: ContextUsersCollectService,
        context_template_mail_service: ContextTemplateCollectService,
    ):
        self.db_manager = db_manager
        self.user_service = context_user_service
        self.template_mail_service = context_template_mail_service

    async def handler_event_welcome(self, message: DeliveredMessage):
        content: dict = orjson.loads(message.body)
        print(content)
        user_id: str = content["user_id"]
        user = await self.user_service.get_user(user_id)
        if user:
            # TODO надо знать id template mail
            template = await self.template_mail_service.get_template_mail("1")
            html_mail = await self.craft_template(template, user)
            await self.build_notification(
                content, user, html_mail, settings.worker_mongo_collection_notifications
            )

    async def handler_event_personal_selection(self, message: DeliveredMessage):
        message_body = orjson.loads(message.body)
        for content in message_body:
            user_id = content["user_id"]
            user = await self.user_service.get_user(user_id)
            if user:
                # TODO надо знать id template mail
                template = await self.template_mail_service.get_template_mail("3")
                html_mail = await self.craft_template(template, user)
                await self.build_notification(
                    message_body,
                    user,
                    html_mail,
                    settings.worker_mongo_collection_notifications,
                )

    async def handler_event_bulk_mails(self, message: DeliveredMessage):
        message_body = orjson.loads(message.body)
        group_id = message_body["group_id"]
        print(message_body)
        # TODO в апи юзер преферренс нужна ручка
        # users = await self.user_service.get_users(group_id=group_id)
        # if users:
        #     for user in users:
        #         template = await self.template_mail_service.get_template_mail('4')
        #         html_mail = await self.craft_template(template, user)
        #         await self.build_notification(message_body,
        #                                       user,
        #                                       html_mail,
        #                                       settings.worker_mongo_collection_notifications)

    async def handler_event_mail(self, message: DeliveredMessage):
        content = orjson.loads(message.body)
        template = await self.template_mail_service.get_template_mail("5")
        html_mail = await self.craft_template(template, content)
        await self.build_notification(
            content, content, html_mail, settings.worker_mongo_collection_notifications
        )

    async def handler_event_like(self, message: DeliveredMessage):
        message_body = orjson.loads(message.body)
        await self.update_or_create_notification_like(
            settings.worker_mongo_collection_notifications,
            message_body["user_id"],
            message_body["review_id"],
        )

    @staticmethod
    async def craft_template(template_string: str, context: dict):
        template = Template(template_string)
        content = template.render(context)
        return content

    async def build_notification(
        self, content: dict, user: dict, html_mail: str, collection_name: str
    ):
        utc_time = get_current_utc_datetime()
        notification = {
            "content": content,
            "status_id": 1,
            "type_id": 1,
            "text_emai": html_mail,
            "last_update": utc_time,
            "last_notification_update": utc_time,
        }
        notification_id = self.db_manager.insert_one(collection_name, notification)
        send_email.apply_async(
            (user["email"], html_mail, "Уведомление", str(notification_id))
        )

    async def update_or_create_notification_like(
        self, collection_name: str, user_id: str, review_id: str
    ):
        notification_like = self.db_manager.check_like(
            collection_name, user_id, review_id
        )
        if notification_like:
            self.db_manager.update_like_by_id(collection_name, notification_like["_id"])
        else:
            content = {
                "user_id": user_id,
                "review_id": review_id,
                "likes_count_new": 1,
                "likes_count_old": 1,
            }
            template = await self.template_mail_service.get_template_mail("2")
            html_mail = await self.craft_template(template, content)
            utc_time = get_current_utc_datetime()
            notification = {
                "content": content,
                "status_id": 1,
                "type_id": 1,
                "text_emai": html_mail,
                "last_update": utc_time,
                "last_notification_update": utc_time,
            }
            self.db_manager.insert_one(collection_name, notification)


@lru_cache(maxsize=None)
def get_event_handler_service():
    db_manager = get_db_manager()
    context_user_service = get_context_user_service()
    context_template_mail_service = get_context_template_service()
    return EventHandler(
        db_manager=db_manager,
        context_user_service=context_user_service,
        context_template_mail_service=context_template_mail_service,
    )
