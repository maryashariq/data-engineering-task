# tests/test_app.py
# tests for src/app.py

import pytest
from src.app import root, average_reviews


def test_root():
    rsp = root()
    assert rsp.data.decode("utf8") == "It's alive!", "Unexpected response message"
    assert rsp.status_code == 200, "Status code was not 200"


