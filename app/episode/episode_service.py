import requests
from app.episode.episode import Episode
from app.bbdd_RickAndMorty.bbdd_RickMorty_service import SqliteService

class EpisodeService:
    def __init__(self):
        pass


    @staticmethod
    def data_episode(baseurl, endpoint):
        path = (baseurl + endpoint)
        r = requests.get(path)
        data_episode = r.json()
        for j in data_episode['results']:
            episodes = Episode((j['name']))
            SqliteService.insert_episode(episodes.name)
        return 'Insertados datos en la tabla episodes'
