from pymongo import MongoClient
import names

import os
import time
import random
import logging
import sys
from datetime import datetime


# Logging stuff
logger = logging.getLogger()
streamHandler = logging.StreamHandler(stream=sys.stdout)
streamHandler.setFormatter(logging.Formatter(
    fmt='[%(asctime)s: %(levelname)s] %(message)s'))
logger.addHandler(streamHandler)

# Mongo credentials
MONGO_USERNAME = os.environ["MONGO_USERNAME"]
MONGO_PASSWORD = os.environ["MONGO_PASSWORD"]
MONGO_PORT = os.environ["MONGO_PORT"]
# Mongo connection
mongo_url = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@localhost:{MONGO_PORT}/"
client = MongoClient(mongo_url)

db = client["db_1"]
clients_data_collection = db["clients_data"]

if __name__ == "__main__":
    while True:
        # Just creating random records
        record = {
            "name": names.get_full_name(),
            "operation_hash": '0x'+str(random.getrandbits(128)),
            "operation_value": random.randint(1, 100000),
            "dt": datetime.strftime(datetime.now(), "%d/%b/%Y %H:%M:%S")
        }
        # Put them into mongodb collection
        clients_data_collection.insert_one(record)
        logger.info("Added record to collection")
        # And waiting random time
        delay = random.randint(3, 10)
        logger.info(f"Waiting for {delay} seconds until next record")
        time.sleep(delay)
