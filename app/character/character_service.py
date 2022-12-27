import requests
from app.character.character import Character
from app.bbdd_RickAndMorty.bbdd_RickMorty_service import SqliteService

class RickAndMortyService:
    def __init__(self):
        pass

    @staticmethod
    def data_character(baseurl, endpoint):
        path = (baseurl + endpoint)
        r = requests.get(path)
        data_character = r.json()
        for j in data_character['results']:
            characters = Character((j['id']), (j['name']), (j['location']['name']))
            SqliteService.insert_character(characters.name, characters.location)
        return 'Insertados datos en la tabla characters'
