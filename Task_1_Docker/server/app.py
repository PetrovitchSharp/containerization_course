from fastapi import FastAPI
import uvicorn
from pymongo import MongoClient
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

import os
import logging
import sys

SERVER_PORT = os.environ["SERVER_PORT"]
MONGO_PORT = os.environ["MONGO_PORT"]
MONGO_USERNAME = os.environ["MONGO_USERNAME"]
MONGO_PASSWORD = os.environ["MONGO_PASSWORD"]

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])

# Logging stuff
logger = logging.getLogger()
streamHandler = logging.StreamHandler(stream=sys.stdout)
streamHandler.setFormatter(logging.Formatter(
    fmt='[%(asctime)s: %(levelname)s] %(message)s'))
logger.addHandler(streamHandler)

# Mongo connection
mongo_url = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@localhost:{MONGO_PORT}/"
client = MongoClient(mongo_url)

db = client["db_1"]
clients_data_collection = db["clients_data"]


@app.get("/get_data")
async def get_lido_validators_share() -> JSONResponse:
    cursor = clients_data_collection.find({}, {'_id':0})
    records = list(cursor)

    logger.info(f"Found {len(records)} records in db")
    
    res = jsonable_encoder(records)
    return JSONResponse(res)


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=int(SERVER_PORT))