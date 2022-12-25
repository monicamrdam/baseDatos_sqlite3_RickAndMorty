import requests

class EpisodeClient:
    def __init__(self):
        pass

    @staticmethod
    def base_url():
        return 'https://rickandmortyapi.com/api/'

    @staticmethod
    def end_point_episode():
        return 'episode'

    @staticmethod
    def main_path(baseurl, endpoint):
        r = requests.get(baseurl + endpoint)
        return r.json()