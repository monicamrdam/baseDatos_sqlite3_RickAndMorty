import requests
from app.character.character import Character
from app.character.rick_and_morty_client import  RickAndMortyClient

class RickAndMortyService:
    def __init__(self):
        pass

    @staticmethod
    def insert_character(name, location):
        db = RickAndMortyClient.get_db()
        cursor = db.cursor()
        statement = "INSERT INTO characters (name, location) VALUES (?,?)"
        cursor.execute(statement, [name, location])
        db.commit()

    @staticmethod
    def data_character(baseurl, endpoint):
        path = (baseurl + endpoint)
        r = requests.get(path)
        data_character = r.json()
        for j in data_character['results']:
            characters = Character((j['id']), (j['name']), (j['location']['name']))
            RickAndMortyService.insert_character(characters.name, characters.location)
        return 'Insertados datos en la tabla characters'
