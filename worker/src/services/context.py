from functools import lru_cache

from core.config import settings
from services.base import BaseContextCollectService


class ContextUsersCollectService(BaseContextCollectService):
    async def get_user(self, user_id: str):
        url_params = f'/api/v1/notification_preference/users/{user_id}'
        user = await self.create_get_response(url_params=url_params)
        if self.is_personal_notification(user):
            return user
        return None

    async def get_users(self, group_id: str = None):
        url_params = '/api/v1/notification_preference/users'
        params_request = None
        if group_id:
            params_request = {'group_id': group_id}
        users = await self.create_get_response(url_params, params_request)
        actual_users = []
        for user in users:
            if self.is_personal_notification(user):
                actual_users.append(user)
        if len(actual_users) > 0:
            return actual_users
        return None

    @staticmethod
    def is_personal_notification(user: dict):
        if user['allow_personal_notifications']:
            return True
        return False


class ContextTemplateCollectService(BaseContextCollectService):
    async def get_template_mail(self, template_mail_id: str = None):
        url_params = f'/api/v1/email-template/?search={template_mail_id}'
        template = await self.create_get_response(url_params=url_params)
        if template:
            return template[0]['html_text']
        return '{{content}}'


@lru_cache(maxsize=None)
def get_context_user_service():
    context_user = ContextUsersCollectService(settings.user_preference_api_url)
    return context_user


@lru_cache(maxsize=None)
def get_context_template_service():
    # TODO ссылку надо поменять
    context_template = ContextTemplateCollectService(settings.mailer_panel_api_url)
    return context_template
