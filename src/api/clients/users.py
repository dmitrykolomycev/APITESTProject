suffix_url = "api/users"

def post_users(client, name: str, surname: str, middle_name: str, email: str, username: str, password: str,
               is_subscribed: bool = True):
    json_body = {
        "name": name,
        "surname": surname,
        "middleName": middle_name,
        "email": email,
        "username": username,
        "password": password,
        "isSubscribed": is_subscribed
    }

    return client.post(suffix_url, json=json_body)

def get_users(client, username: str, page: int = 1, size: int = 50):
    params = {
        "query": username,
        "page": page,
        "size": size
    }

    return client.get(suffix_url, params=params)

def put_users(client, name: str,  middle_name: str, surname: str):
    json_body = {
        "name": name,
        "surname": surname,
        "middleName": middle_name
    }

    return client.put(suffix_url, json=json_body)

def get_users_me(client):
    return client.get(f"{suffix_url}/me")