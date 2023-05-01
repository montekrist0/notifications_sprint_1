from functools import lru_cache

from jinja2 import Template
from pymongo.database import Database

from services.db_manager import get_db_manager
from services.tools import get_current_utc_datetime
from services.context import (
    ContextTemplateCollectService,
    get_context_template_service
)
from services.base import BaseNotificationService
from tasks import send_email


class NotificationEmailService(BaseNotificationService):

    def __init__(self, db_manager: Database,
                 context_template_mail_service: ContextTemplateCollectService, ):
        self.db_manager = db_manager
        self.template_mail_service = context_template_mail_service

    async def send_notification(self, template_id: str, content: dict, user: dict, collection_name: str):
        template = await self.template_mail_service.get_template_mail(template_id)
        html_mail = self.craft_template(template, content)
        notification_id = await self.build_notification(content, html_mail, collection_name)
        await self.send_notification_on_email(user['email'], html_mail, str(notification_id))

    async def build_notification(
            self, content: dict, html_mail: str, collection_name: str
    ):
        utc_time = get_current_utc_datetime()
        notification = {
            'content': content,
            'status_id': 1,
            'type_id': 1,
            'text_emai': html_mail,
            'last_update': utc_time,
            'last_notification_update': utc_time,
        }
        notification_id = self.db_manager.insert_one(collection_name, notification)
        return notification_id

    async def update_or_create_notification_like(
            self, collection_name: str, user_id: str, review_id: str
    ):
        notification_like = self.db_manager.check_like(
            collection_name, user_id, review_id
        )
        if notification_like:
            self.db_manager.update_like_by_id(collection_name, notification_like['_id'])
        else:
            content = {
                'user_id': user_id,
                'review_id': review_id,
                'likes_count_new': 1,
                'likes_count_old': 1,
            }
            template = await self.template_mail_service.get_template_mail('2')
            html_mail = self.craft_template(template, content)
            utc_time = get_current_utc_datetime()
            notification = {
                'content': content,
                'status_id': 1,
                'type_id': 1,
                'text_emai': html_mail,
                'last_update': utc_time,
                'last_notification_update': utc_time,
            }
            self.db_manager.insert_one(collection_name, notification)

    @staticmethod
    def craft_template(template_string: str, context: dict):
        template = Template(template_string)
        content = template.render(context)
        return content

    @staticmethod
    async def send_notification_on_email(address: str, body: str, notification_id: str):
        send_email.apply_async(
            (address, body, 'Уведомление', notification_id)
        )


@lru_cache(maxsize=None)
def get_notification_email_service():
    db_manager = get_db_manager()
    context_template_mail_service = get_context_template_service()
    return NotificationEmailService(
        db_manager=db_manager,
        context_template_mail_service=context_template_mail_service
    )
