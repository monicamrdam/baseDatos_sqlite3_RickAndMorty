from app.artist.spotify_client import SpotifyClient
from app.artist.artist import Artist
from app.artist.artist_topTracks import TopTracks
from app.bbdd_Spotify.bbdd_Spotify_service import SqliteService

class SpotifyService:
    def __init__(self):
        pass

    @staticmethod
    def get_artist_popularity(name_artist):
        all_tracks = []
        data_artist = SpotifyClient.url_artist(name_artist)
        data_top_track = SpotifyClient.url_top_track(name_artist)
        if not ('tracks' in data_top_track) or ((len(data_top_track['tracks'])) <5 ) :
            return []
        else:
            for track in data_top_track['tracks'][:5]:
                SqliteService.insert_top_artist(name_artist, track['name'], track['popularity'])
                tracks_data = TopTracks(track['name'], track['popularity'])
                artist_track = {
                    'name': tracks_data.name,
                    'popularity': tracks_data.popularity,
                }
                all_tracks.append(artist_track)
            SqliteService.insert_artist(data_artist['id'],data_artist['name'],data_artist['popularity'])
            data_artist = Artist(data_artist['name'], data_artist['popularity'])
            artist = {
                'name': data_artist.name,
                'popularity': data_artist.popularity,
                'popularTracks': all_tracks
            }
            return artist
