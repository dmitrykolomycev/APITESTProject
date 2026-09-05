suffix_url = "api/random"

def get_random_character(client):

    return client.get(f"{suffix_url}/character")



