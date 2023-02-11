from typing import List, Optional

import databases
import sqlalchemy
from fastapi import FastAPI
from src.config import config

import ormar

app = FastAPI()
metadata = sqlalchemy.MetaData()
database = databases.Database(config['db'])
app.state.database = database

async def make_tables():
    import sqlalchemy
    # get your database url in sqlalchemy format - same as used with databases instance used in Model definition
    engine = sqlalchemy.create_engine(config['db'])
    # note that this has to be the same metadata that is used in ormar Models definition
    metadata.create_all(engine)


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()
    await make_tables()
    


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()

import src.routes