from contextlib import asynccontextmanager
import databases
import sqlalchemy
from fastapi import FastAPI
from src.config import config
from fastapi_pagination import add_pagination
import os

import ormar


@asynccontextmanager
async def lifespan(app: FastAPI):
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()
    yield
    if database_.is_connected:
        await database_.disconnect()


app = FastAPI(lifespan=lifespan)
metadata = sqlalchemy.MetaData()
database = databases.Database(config['db' if not bool(os.environ.get('TESTING')) else 'test_db'])
app.state.database = database
add_pagination(app)

import src.routes