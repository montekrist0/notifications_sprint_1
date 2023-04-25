import requests

from config.settings import Settings

from utils.backoff import backoff
from utils.logger import logger


class AuthExtract:
    def __init__(self, start_id: int, end_id: int, url: str = Settings().AUTH_HOST_PORT,
                 uri: str = Settings().USERINFO_ENDPOINT):
        """

        :param start_id: начальный айди юзера для запроса
        :param end_id: конечный айди юзера, который бует включен в запрос
        :param url: хост:порт сервиса Auth
        :param uri: endpoint нужного обработчика в Auth (который отдаёт информацию о юзере)
        """
        self._url = f'http://{url}/{uri}/{start_id}/{end_id}'
        self._start = start_id
        self._end = end_id
        self._result = self._fetch_data()

    @backoff()
    def _fetch_data(self) -> list[dict]:
        response = requests.get(self._url)
        if b'Not found' in response.content:
            raise ValueError
        logger.info(f'users info from id {self._start} to id {self._end} fetched')
        logger.debug(response.json())
        return response.json()

    @property
    def results(self) -> list[dict]:
        return self._result
