from app.RickAndMortySpotify.artist.artist_client import SpotifyClient
from app.RickAndMortySpotify.artist.artist import Artist, TopTracks
from app.RickAndMortySpotify.artist.artist_repository import ArtistRepository

class SpotifyService:

    @staticmethod
    def result_search(name_artist):
        result= ArtistRepository.get_one_where_name_artist(name_artist)
        result_=result.fetchone()
        if result_ is None:
            name_artist_search=SpotifyService.insert_artist_popularity(name_artist)
            print ('Datos insertados en la db de ' + name_artist)
            result = ArtistRepository.get_one_where_name_artist(name_artist_search)
            result_ = result.fetchone()
            artist_search = Artist(result_[1], result_[2])
            return artist_search.serialize()
        else:
            artist_search=Artist(result_[1], result_[2])
            print ('Datos recuperados en la db de ' + name_artist)
            return artist_search.serialize()

    @staticmethod
    def insert_artist_popularity(name_artist):
        data_artist = SpotifyClient.url_artist(name_artist)
        uuid_artist= ArtistRepository.get_uuid(10)
        ArtistRepository.insert_artist(uuid_artist, (data_artist['name']).casefold(), data_artist['popularity'])
        data_top_track = SpotifyClient.url_top_track(name_artist)
        if not ('tracks' in data_top_track) or ((len(data_top_track['tracks'])) <5 ) :
            return []
        else:
            for track in data_top_track['tracks'][:5]:
                ArtistRepository.insert_top_tracks(ArtistRepository.get_uuid(10),uuid_artist, track['name'], track['popularity'])
        return (data_artist['name']).casefold()


    @staticmethod
    def get_artist_popularity(name_artist):
        all_tracks = []
        data_artist = SpotifyClient.url_artist(name_artist)
        data_top_track = SpotifyClient.url_top_track(name_artist)
        if not ('tracks' in data_top_track) or ((len(data_top_track['tracks'])) <5 ) :
            return []
        else:
            for track in data_top_track['tracks'][:5]:
               # SqliteService.insert_top_artist(name_artist, track['name'], track['popularity'])
                tracks_data = TopTracks(track['name'], track['popularity'])
                artist_track = {
                    'name': tracks_data.name,
                    'popularity': tracks_data.popularity,
                }
                all_tracks.append(artist_track)
            #SqliteService.insert_artist(data_artist['id'],data_artist['name'],data_artist['popularity'])
            data_artist = Artist(data_artist['name'], data_artist['popularity'])
            artist = {
                'name': data_artist.name,
                'popularity': data_artist.popularity,
                'popularTracks': all_tracks
            }
            return artist