from aiormq.abc import DeliveredMessage
import orjson

from core.config import settings
from services.context import (get_context_user_service,
                              get_context_template_service)
from tasks import send_email
from services.craft_mail import craft_template
from services.db_manager import get_db_manager
from services.tools import get_current_utc_datetime

context_user = get_context_user_service()
context_template_mail = get_context_template_service()

mongo_db_manager = get_db_manager()


async def event_welcome(message: DeliveredMessage):
    message_body = orjson.loads(message.body)
    user_id = message_body['user_id']
    user = await context_user.get_user(user_id)
    if user:
        # TODO надо знать id template mail
        template = await context_template_mail.get_template_mail(1)
        html_mail = craft_template(template, user)
        utc_time = get_current_utc_datetime()
        notification = {
            'content': message_body,
            'status_id': 1,
            'type_id': 1,
            'text_emai': html_mail,
            'last_update': utc_time,
            'last_notification_update': utc_time
        }
        notification_id = mongo_db_manager.insert_one(settings.worker_mongo_collection_notifications, notification)
        send_email.apply_async((user['email'], html_mail, 'Привет', str(notification_id)))


async def event_like(message: DeliveredMessage):
    user = orjson.loads(message.body)
    user_id = user['user_id']
    user = await context_user.get_user(user_id)
    if user:
        # TODO надо знать id template mail
        template = await context_template_mail.get_template_mail(2)
        html_mail = craft_template(template, user)
        utc_time = get_current_utc_datetime()
        # TODO пока не знаю как или воркер будет это обрабатывать


async def event_personal_selection(message: DeliveredMessage):
    message_body = orjson.loads(message.body)
    for personal_selection in message_body:
        user_id = personal_selection['user_id']
        user = await context_user.get_user(user_id)
        if user:
            # TODO надо знать id template mail
            template = await context_template_mail.get_template_mail(3)
            html_mail = craft_template(template, user)
            utc_time = get_current_utc_datetime()
            notification = {
                'content': personal_selection,
                'status_id': 1,
                'type_id': 1,
                'text_emai': html_mail,
                'last_update': utc_time,
                'last_notification_update': utc_time
            }
            notification_id = mongo_db_manager.insert_one(settings.worker_mongo_collection_notifications, notification)
            send_email.apply_async((user['email'], html_mail, 'Привет', str(notification_id)))


async def event_bulk_mails(message: DeliveredMessage):
    print(f"     Message body is: {message.body!r}")
    # TODO получить по id данные пользователя в сервисе с предпочтениями
    # TODO получить шаблон пиьсьма


async def event_mail(message: DeliveredMessage):
    user = orjson.loads(message.body)
    user_id = user['user_id']
    user = await context_user.get_user(user_id)
    if user:
        # TODO надо знать id template mail
        template = await context_template_mail.get_template_mail()
        # тут будет создаваться задача
