import orjson
from django.db.models.signals import post_save
from django.dispatch import receiver

from config.components.common import EVENT_API_BULK_MAILS, EVENT_API_ONE_MAIL
from mailer.tasks import send_event
from mailer.models import MassNotification, IndividualNotification


@receiver(post_save, sender=MassNotification)
@receiver(post_save, sender=IndividualNotification)
def run_task_event(sender, instance, **kwargs):
    url_event = None
    body_request = None
    delay = 0
    if sender == IndividualNotification:
        url_event = EVENT_API_ONE_MAIL
        body_request = {
            'user_name': instance.username,
            'email': instance.email,
            'content': instance.body,
        }
        delay = instance.delay
    if sender == MassNotification:
        url_event = EVENT_API_BULK_MAILS
        body_request = {
            'group_id': instance.group_id,
            'content': instance.body,
        }
        delay = instance.delay
    send_event.apply_async(args=(url_event, body_request), countdown=delay)
