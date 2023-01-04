import requests
from app.episode.episode import Episode
from app.episode.episode_client import EpisodeClient

class EpisodeService:
    def __init__(self):
        pass

    @staticmethod
    def insert_episode(name):
        db = EpisodeClient.get_db()
        cursor = db.cursor()
        statement = "INSERT INTO episodes (name) VALUES (?)"
        cursor.execute(statement, [name])
        db.commit()


    @staticmethod
    def data_episode(baseurl, endpoint):
        path = (baseurl + endpoint)
        r = requests.get(path)
        data_episode = r.json()
        for j in data_episode['results']:
            episodes = Episode((j['name']))
            EpisodeService.insert_episode(episodes.name)
        return 'Insertados datos en la tabla episodes'
