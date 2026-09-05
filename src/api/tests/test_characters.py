import os.path
from pathlib import Path
from urllib.parse import urlparse

import allure
import pytest

from src.api.clients.characters import get_characters_id, get_characters
from src.api.helpers.api_client import get_client
from src.api.helpers.download_file import download_file
"""Готова все и все оабьоатет, можно лить"""

class TestCharacters:

    client = get_client()
    @allure.story("Получение информации о персонаже по ИД")
    @allure.tag("API")
    @allure.link(url="https://hello-world.com")

    @pytest.mark.parametrize("character_id, character_name", [(1, "Philip J. Fry"),
                                                              (16, "Bender Bending Rodríguez"),
                                                              (425, "Turanga Leela")])
    def test_get_character_by_id(self, character_id, character_name):
        """Проверка получения информации о персонаже по ИД."""

        response = get_characters_id(self.client, character_id)
        assert response.status_code == 200
        assert response.json()["name"] == character_name
        assert isinstance(response.json()["id"], int)

    @allure.story("Попытка получить информацию о несуществующем ИД")
    def test_negative_get_character_by_id(self):
        """Негативная проверка получения информации о персонаже по ИД."""

        response = get_characters_id(self.client, 0)
        assert response.status_code == 404
        assert response.json()["detail"] == "Character not found"

    @allure.story("Получение списка персонажей")
    def test_get_characters(self):
        """Получение списка персонажей."""

        response = get_characters(self.client)
        assert response.status_code == 200
        assert len(response.json()["items"]) == 50

    @allure.story("Получение изображения персонажа")
    @allure.issue(url="https://example.com", name="Ссылка на баг")
    def test_download_image(self):
        """Загрузка изображения."""

        response = get_characters_id(self.client, 1)
        image_url = response.json()["image"]

        filename = Path(urlparse(image_url).path).name
        image_response = self.client.get(image_url)

        image_content = image_response.content

        download_file(filename, image_content)

        assert os.path.exists(filename), "Файл не был сохранен"