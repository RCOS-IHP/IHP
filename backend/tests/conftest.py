from enum import Enum
from fastapi.testclient import TestClient
from httpx import Client

class TestClient(Client):
    def request(self, method: str, url, **kwargs):
        if url.startswith("/"):
            url = "http://localhost:8068" + url
        return super().request(method, url, **kwargs)

client = TestClient()

def encoder_for_enums(obj):
    if isinstance(obj, Enum):
        return obj.value
    return obj