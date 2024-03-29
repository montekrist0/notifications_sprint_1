from abc import (ABC,
                 abstractmethod)
import aiohttp


class BaseContextCollectService:
    def __init__(self, url: str):
        self.url: str = url

    async def create_get_response(
            self, url_params: str = None, params_request: dict = None
    ):
        async with aiohttp.ClientSession() as session:
            url = self.url
            if url_params:
                url = url + url_params
            try:
                async with session.get(url, params=params_request) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data
                    return None
            except aiohttp.ClientOSError:
                return None


class BaseNotificationService(ABC):

    @abstractmethod
    async def build_notification(self, *args, **kwargs):
        pass

    @abstractmethod
    async def update_or_create_notification_like(self, *args, **kwargs):
        pass

    @abstractmethod
    def craft_template(self, *args, **kwargs):
        pass

    @abstractmethod
    async def send_notification(self, *args, **kwargs):
        pass
