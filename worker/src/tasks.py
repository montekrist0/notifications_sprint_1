import bson

from celery import Celery
import sib_api_v3_sdk
from sib_api_v3_sdk import SendSmtpEmailSender, SendSmtpEmailTo
from sib_api_v3_sdk.rest import ApiException

from core.config import settings
from core.config import broker_url
from services.db_manager import get_db_manager

app = Celery("tasks", broker=broker_url)

mongo_db_manager = get_db_manager()


@app.task(queue="tasks")
def send_email(address: str, body: str, subject: str, notification_id):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key["api-key"] = settings.sendinblue_apikey
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        sender=SendSmtpEmailSender(email=settings.sendinblue_email_sender),
        to=[SendSmtpEmailTo(email=address), ],
        subject=subject,
        html_content=body,
    )
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        mongo_db_manager.update_status_by_id(settings.worker_mongo_collection_notifications, notification_id, 3)
    except ApiException as e:
        mongo_db_manager.update_status_by_id(settings.worker_mongo_collection_notifications, notification_id, 2)
        print(e)
        pass
