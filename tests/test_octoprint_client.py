import pytest
from src.octoprint_client import OctoPrintClient

class DummyResponse:
    def __init__(self, status_code):
        self.status_code = status_code

class DummyRequests:
    def __init__(self, status_code=204):
        self._status_code = status_code
        self.last_json = None
        self.last_headers = None
    def post(self, url, json, headers):
        self.last_json = json
        self.last_headers = headers
        return DummyResponse(self._status_code)

@pytest.fixture(autouse=True)
def patch_requests(monkeypatch):
    dummy = DummyRequests()
    monkeypatch.setattr("src.octoprint_client.requests", "post", dummy.post)
    return dummy

def test_send_command_success():
    client = OctoPrintClient("ip", "port", "key")
    assert client.send_command({"command": "jog", "x": 10}) is True

def test_send_command_failure(monkeypatch):
    class FailRequests:
        def post(self, url, json, headers):
            return DummyResponse(400)
    monkeypatch.setattr("src.octoprint_client.requests", "post", FailRequests().post)
    client = OctoPrintClient("ip", "port", "key")
    assert client.send_command({"command": "jog", "x": 10}) is False

def test_send_command_exception(monkeypatch):
    def raise_exc(*a, **kw):
        raise Exception("fail")
    monkeypatch.setattr("src.octoprint_client.requests", "post", raise_exc)
    client = OctoPrintClient("ip", "port", "key")
    assert client.send_command({"command": "jog", "x": 10}) is False
