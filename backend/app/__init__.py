from typing import List, Optional

import databases
import sqlalchemy
from fastapi import FastAPI
from app.config import config

import ormar

app = FastAPI()
metadata = sqlalchemy.MetaData()
database = databases.Database(config['db'])
app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()

@app.get("/")
def root():
    return {"message": "Hello World"}