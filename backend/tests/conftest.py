from enum import Enum
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def encoder_for_enums(obj):
    if isinstance(obj, Enum):
        return obj.value
    return obj