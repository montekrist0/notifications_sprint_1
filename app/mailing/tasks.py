import re
from pprint import pprint

from django.conf import settings
from celery import shared_task
import sib_api_v3_sdk
from sib_api_v3_sdk import SendSmtpEmailTo, SendSmtpEmailSender
from sib_api_v3_sdk.rest import ApiException


@shared_task()
def send_email(address: str, body: str, subject: str):
    """
    функция отправляет сформированное письмо через сервис sendgrid
    :param address: e-mail address
    :param body: html e-mail body
    :param subject: e-mail subject
    :return:
    """
    if not re.match(r"^[\w.-]+@[\w.-]+\.\w+$", address):
        raise ValueError("""'address' param must be valid e-mail address""")

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.SENDINBLUE_APIKEY
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        sender=SendSmtpEmailSender(email='sender@ctube-study.ru'),
        to=[SendSmtpEmailTo(email=address), ], # можно отправлять list[SendSmtpEmailTo], для массовых адресатов, но лучше
        # посмотреть доки на batch рассылки
        subject=subject,
        html_content=body
    )

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionalEmailsApi->send_transac_email: %s\n" % e)