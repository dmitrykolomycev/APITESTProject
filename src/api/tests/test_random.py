from src.api.clients.random import get_random_character
from src.api.helpers.api_client import get_client

class TestRandom:
    client = get_client(timeout=30)


    def test_get_random_character(self, api_client):
        """Получение случайного персонажа по ИД"""

        response = get_random_character(self.client)
        assert response.status_code == 200




