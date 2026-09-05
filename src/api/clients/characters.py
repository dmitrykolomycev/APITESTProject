suffix_url = "api/characters"

def get_characters_id(client, character_id ):

        return client.get(f"{suffix_url}/{character_id}")

def get_characters(client, order_by: str = "id", order_by_direction: str = "asc", page: int = 1, size: int = 50,
                   gender: str = None, species: str = None):
        params = {
                "orderBy": order_by,
                "orderByDirection": order_by_direction,
                "page": page,
                "size": size,
        }
        if gender:
                params["gender"] = gender
        if species:
                params["species"] = species

        return client.get(suffix_url, params=params)





