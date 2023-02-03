from typing import List, Optional

import databases
import sqlalchemy
from fastapi import FastAPI

import ormar

app = FastAPI()
metadata = sqlalchemy.MetaData()
database = databases.Database("sqlite://./test.db")
app.state.database = database