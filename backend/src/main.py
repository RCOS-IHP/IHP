import databases
import sqlalchemy
from fastapi import FastAPI
from src.config import config
from fastapi_pagination import add_pagination

import ormar

app = FastAPI()
metadata = sqlalchemy.MetaData()
database = databases.Database(config['db'])
app.state.database = database
add_pagination(app)


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

import src.routes