import requests


class RickAndMortyClient:
    def __init__(self):
        pass

    @staticmethod
    def base_url():
        return 'https://rickandmortyapi.com/api/'

    @staticmethod
    def end_point_character():
        return 'character'

    @staticmethod
    def main_path(baseurl, endpoint):
        r = requests.get(baseurl + endpoint)
        return r.json()
