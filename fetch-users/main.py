import time

from extract import AuthExtract
from load import MongoLoad
from config.settings import Settings
from utils.mongo import MongoConnector
from utils.logger import logger
from control import Searcher


SETTINGS = Settings()

if __name__ == '__main__':
    connector = MongoConnector(mongo_host=SETTINGS.MONGO_HOST, mongo_port=SETTINGS.MONGO_PORT,
                                  database=SETTINGS.DB_NAME)
    db_client = connector.client
    start_id = Searcher(db_connection=db_client, collection=SETTINGS.COLLECTION).id
    end_id = start_id + SETTINGS.BATCH_SIZE
    error_counter = int()

    while True:
        try:
            fetched_data = AuthExtract(start_id=start_id, end_id=end_id).results
            error_counter = 0
            MongoLoad(collection=SETTINGS.COLLECTION, data=fetched_data, mongo_db_connector=db_client)
            start_id = Searcher(db_connection=db_client, collection=SETTINGS.COLLECTION).id
            end_id = start_id + SETTINGS.BATCH_SIZE

        except ValueError:
            error_counter += 1
            if start_id == end_id:
                start_id += 1
                end_id = start_id
            else:
                end_id = start_id

        finally:
            logger.info(f'sleep to {SETTINGS.SLEEP} secs...')
            time.sleep(SETTINGS.SLEEP)
            if error_counter > 100:
                logger.info('waiting for new users, sleep ...')
                time.sleep(300)

    connector.close()

