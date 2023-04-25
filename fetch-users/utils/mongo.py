from pymongo import MongoClient
from pymongo.database import Database


class MongoConnector:
    def __init__(self, mongo_host: str, mongo_port: int = 27017,
                 database: str = 'users-database'):
        """

        :param mongo_host: Mongo host
        :param mongo_port: Mongo port
        :param database: Mongo database to connect
        """
        self._host = mongo_host
        self._port = mongo_port
        self._database = database
        self._client = self._get_client()
        self._db_client = self._checkout_database()

    def _get_client(self):
        return MongoClient(self._host, self._port)

    def _checkout_database(self):
        return self._client[self._database]

    def close(self):
        self._client.close()

    @property
    def client(self) -> Database:
        return self._db_client
