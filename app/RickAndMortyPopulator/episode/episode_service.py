import requests
import random
import string
from app.RickAndMortyPopulator.episode.episode import Episode
from app.RickAndMortyPopulator.episode.episode_client import EpisodeClient

class EpisodeService:
    def __init__(self):
        pass

    @staticmethod
    def get_uuid(num_dig):
        uuid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num_dig))
        return uuid


    @staticmethod
    def insert_episode(uuid,name):
        db = EpisodeClient.get_db()
        cursor = db.cursor()
        statement = "INSERT INTO episodes (uuid, name) VALUES (?,?)"
        cursor.execute(statement, [uuid,name])
        db.commit()


    @staticmethod
    def data_episode(baseurl, endpoint):
        path = (baseurl + endpoint)
        r = requests.get(path)
        data_episode = r.json()
        for j in data_episode['results']:
            episodes = Episode((j['name']))
            EpisodeService.insert_episode(EpisodeService.get_uuid(10), episodes.name)
        return 'Insertados datos en la tabla episodes'
