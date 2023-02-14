from json import dumps, JSONEncoder
from typing import Any
from pydantic import BaseModel


class BaseModelEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, BaseModel):
            return o.dict()
        return super().default(o)

def convert_to_json(data: Any):
    if data is None or isinstance(data, (int, float)):
        return data
    return dumps(data, cls=BaseModelEncoder)