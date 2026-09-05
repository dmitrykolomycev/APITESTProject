import pytest

from src.api.helpers.api_client import get_client


@pytest.fixture
def api_client():
    return get_client()