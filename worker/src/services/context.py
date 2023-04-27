from functools import lru_cache

from core.config import settings
from services.base import BaseContextCollectService


class ContextUsersCollectService(BaseContextCollectService):
    async def get_user(self, user_id: str):
        url_params = f"/api/v1/notification_preference/users/{user_id}"
        user = await self.create_get_response(url_params=url_params)
        if self.is_personal_notification(user):
            return user
        return None

    async def get_users(self, group_id: str = None):
        url_params = "/api/v1/notification_preference/users"
        params_request = None
        if group_id:
            params_request = {"group_id": group_id}
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
        if user["allow_personal_notifications"]:
            return True
        return False


class ContextTemplateCollectService(BaseContextCollectService):
    async def get_template_mail(self, template_mail_id: str = None):
        match template_mail_id:
            case "1":
                return "<div>Спасибо за регистрацию {{user_name}}</div>"
            case "2":
                return "<div>вам поставили {{likes_count_new}} лайк(-ов)</div>"
            case "3":
                return "<div>{{user_name}} для вас персональная рассылка</div>"
            case "4":
                return "<div>{{user_name}} массовая рассылка спешил фор ю</div>"
            case "5":
                return "<div>{{user_name}} {{content}}</div>"
            case _:
                return "<div>Hello {{user_name}}</div>"


@lru_cache(maxsize=None)
def get_context_user_service():
    context_user = ContextUsersCollectService(settings.user_preference_api_url)
    return context_user


@lru_cache(maxsize=None)
def get_context_template_service():
    # TODO ссылку надо поменять
    context_template = ContextTemplateCollectService(settings.user_preference_api_url)
    return context_template
