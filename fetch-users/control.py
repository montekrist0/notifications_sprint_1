from pymongo.database import Database
from pymongo import ASCENDING, DESCENDING


class Searcher:
    def __init__(self, db_connection: Database, collection: str):
        """

        :param db_connection: instance Database, so-called 'db-client'
        :param collection: name of collection
        """
        self._db = db_connection
        self._collection = self._db[collection]
        self._id_to_fetch = self._search_first_to_fetch()

    def _search_first_to_fetch(self) -> int:
        return (self._collection.find().sort('id', DESCENDING).limit(1)[0]['id'] + 1) \
            if list(self._collection.find()) else 1

    @property
    def id(self):
        return self._id_to_fetch
