import os
from random import randint

from dotenv import load_dotenv

from src.api.clients.users import post_users, get_users, put_users, get_users_me
from src.api.helpers.api_client import get_client
from src.api.helpers.email import generate_random_email


class TestUsers:
    load_dotenv()
    client = get_client(username=os.getenv("AUTOTEST_USERNAME"), password=os.getenv("AUTOTEST_PASSWORD"))

    def test_create_user(self):
        """Проверка создания пользователя."""

        email = generate_random_email()
        username = f"TestTestov_{randint(1000, 9999)}"

        response = post_users(self.client, name="Test", surname="Testovich", middle_name="Dimas", email=email,
                              password="helloWorld", username=username)

        assert response.status_code == 201

        user_response = get_users(self.client, username=username)

        assert next((user for user in user_response.json()["items"] if user["username"] == username), None), \
            f"Пользователь {username} не был создан"


    def test_change_user(self):
        """Изменяет информацию о пользователе"""

        new_name = f"TestName_{randint(1000, 9999)}"
        new_middlename = f"TestMiddleName_{randint(1000, 9999)}"
        new_surname = f"TestSurname_{randint(1000, 9999)}"

        change_response = put_users(self.client, new_name, new_middlename, new_surname)

        assert change_response.status_code == 200

        user_info = get_users_me(self.client)

        assert user_info.json()["name"] == new_name
        assert user_info.json()["surname"] == new_surname
        assert user_info.json()["middleName"] == new_middlename




