import random
import string
import requests
from app.RickAndMortyPopulator.character.character import Character
from app.RickAndMortyPopulator.character.character_client import  RickAndMortyClient


class RickAndMortyService:
    def __init__(self):
        pass


    @staticmethod
    def get_uuid(num_dig):
        uuid =''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num_dig))
        return uuid

    @staticmethod
    def insert_character(uuid,name, location):
        db = RickAndMortyClient.get_db()
        cursor = db.cursor()
        statement = "INSERT INTO characters (uuid, name, location) VALUES (?,?,?)"
        cursor.execute(statement, [uuid, name, location])
        db.commit()

    @staticmethod
    def data_character(baseurl, endpoint):
        path = (baseurl + endpoint)
        r = requests.get(path)
        data_character = r.json()
        for j in data_character['results']:
            characters = Character(RickAndMortyService.get_uuid(10), (j['name']), (j['location']['name']))
            RickAndMortyService.insert_character(characters.id,characters.name, characters.location)
        return 'Insertados datos en la tabla characters'