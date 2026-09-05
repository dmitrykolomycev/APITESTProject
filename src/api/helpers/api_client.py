import os

import httpx
from dotenv import load_dotenv


def get_token(username: str, password: str):
    """Получение токена.

    :param username имя пользователя
    :param password  пароль
    """

    data = {
        "username": username,
        "password": password
    }

    access_response = httpx.post("https://futuramaapi.com/api/tokens/users/auth", data=data)
    return access_response.json()["access_token"]

def get_client(username: str = None, password: str = None, timeout: int = None):
    """Получение HTTP-клиента

    :param username имя пользователя
    :param password пароль
    :param timeout ожидаемое время ответа от сервера
    """

    load_dotenv()
    if username:
        access_token = get_token(username, password)
        return httpx.Client(base_url=os.getenv("BASE_URL"), timeout=timeout, headers={"Authorization": f"Bearer {access_token}"})
    else:
        return httpx.Client(base_url=os.getenv("BASE_URL"), timeout=timeout)

