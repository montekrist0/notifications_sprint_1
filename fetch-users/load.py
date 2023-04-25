from pymongo import MongoClient, IndexModel, ASCENDING, DESCENDING
from pymongo.errors import ConnectionFailure, DuplicateKeyError
from pymongo.database import Database
from bson.objectid import ObjectId

from utils.backoff import backoff
from utils.logger import logger


class MongoLoad:
    def __init__(self, collection: str, data: list[dict], mongo_db_connector: Database):
        """

        :param collection: name of created / existing collection in Mongo to insert data
        :param data: data to insert in Mongo
        :param mongo_db_connector: connector.client instance
        """
        self._collection = collection
        self._data = data
        self._db_client = mongo_db_connector
        self._db_collection = self._checkout_collection()
        self._inserted_many_resp = self._insert_many()
        self._create_indexes()

    def _checkout_collection(self):
        return self._db_client[self._collection]

    def _create_indexes(self):
        self._db_collection.create_index([('id', ASCENDING)], unique=True, name='id unique constr')
        self._db_collection.create_index([('email', DESCENDING)], unique=False, name='email unique constr')

    @backoff(exception=ConnectionFailure, message=f'Failed connect to Mongo')
    def _insert_many(self):
        inserted_data = list()
        for eachdict in self._data:
            try:
                inserted_data.append(self._db_collection.insert_one(eachdict))
                logger.info(f'document inserted')
                logger.debug(f'inserted document \n {eachdict} \n')
            except DuplicateKeyError:
                logger.debug(f'document with data \n {eachdict} \n exists, skipping...')
                continue
        logger.info(f'data inserted')
        return inserted_data

    @property
    def inserted_many(self) -> list[ObjectId]:
        return self._inserted_many_resp.inserted_ids
