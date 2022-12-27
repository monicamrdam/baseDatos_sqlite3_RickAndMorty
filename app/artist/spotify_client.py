import requests
from config import Config


class SpotifyClient:

    def __init__(self):
        pass

    @staticmethod
    def authorization():
        client_id = Config.CLIENT_ID
        client_secret = Config.CLIENT_SECRET

        auth_url = 'https://accounts.spotify.com/api/token'
        data = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
        }
        auth_response = requests.post(auth_url, data=data)
        access_token = auth_response.json().get('access_token')
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        return headers

    @staticmethod
    def url_search(name_artist):
        base_url = Config.URL_Search
        name = str(name_artist)
        featured_playlists_endpoint = '?q=' + name + '&type=artist'
        featured_playlists_url = ''.join([base_url, featured_playlists_endpoint])
        print(featured_playlists_url)
        response = requests.get(featured_playlists_url, headers=SpotifyClient.authorization())
        if (len(response.json()['artists']['items'])) == 0:
            return str(0)
        else:
            id_artist = response.json()['artists']['items'][0]['id']
            return id_artist

    @staticmethod
    def url_artist(name_artist):
        id_artist = SpotifyClient.url_search(name_artist)
        print(id_artist)
        base_url_artist = Config.URL_Artist
        featured_playlists_endpoint = '/' + id_artist
        featured_playlists_url_artist = ''.join([base_url_artist, featured_playlists_endpoint])
        print(featured_playlists_url_artist)
        response_artist = requests.get(featured_playlists_url_artist, headers=SpotifyClient.authorization())
        return response_artist.json()

    @staticmethod
    def url_top_track(name_artist):
        id_artist = SpotifyClient.url_search(name_artist)
        print(id_artist)
        base_url_artist = Config.URL_Artist
        featured_playlists_endpoint = '/' + id_artist + '/top-tracks?market=ES'
        featured_playlists_url_artist = ''.join([base_url_artist, featured_playlists_endpoint])
        print(featured_playlists_url_artist)
        response_top_tracks = requests.get(featured_playlists_url_artist, headers=SpotifyClient.authorization())
        return response_top_tracks.json()
