from app.RickAndMortySpotify.artist.artist_client import SpotifyClient
from app.RickAndMortySpotify.artist.artist import Artist, TopTracks
from app.RickAndMortySpotify.artist.artist_repository import ArtistRepository


class SpotifyService:

    @staticmethod
    def result_search(name_artist):
        alldata = []
        tracks = []
        result = ArtistRepository.get_one_where_name_artist(name_artist)
        result_ = result.fetchone()
        if result_ is None:
            name_artist_search = SpotifyService.insert_artist_popularity(name_artist)
            print('Datos insertados en la db de ' + name_artist)
            result = ArtistRepository.get_one_where_name_artist(name_artist_search)
            result_ = result.fetchone()
            artist_search = Artist(result_[1], result_[2])
            alldata.append(artist_search.serialize())
            result_track = ArtistRepository.get_track_where_uuid_artist(result_[0])
            for re in result_track.fetchall():
                track_search = (TopTracks(re[2], re[3]))
                tracks.append(track_search.serialize())
            alldata.append(tracks)
            return alldata
        else:
            print('Datos recuperados en la db de ' + name_artist)
            artist_search = Artist(result_[1], result_[2])
            alldata.append(artist_search.serialize())
            result_track = ArtistRepository.get_track_where_uuid_artist(result_[0])
            for re in result_track.fetchall():
                track_search=(TopTracks(re[2],re[3]))
                tracks.append(track_search.serialize())
            alldata.append(tracks)
            return alldata

    @staticmethod
    def insert_artist_popularity(name_artist):
        data_artist = SpotifyClient.url_artist(name_artist)
        uuid_artist = ArtistRepository.get_uuid(10)
        ArtistRepository.insert_artist(uuid_artist, (data_artist['name']).casefold(), data_artist['popularity'])
        data_top_track = SpotifyClient.url_top_track(name_artist)
        if not ('tracks' in data_top_track) or ((len(data_top_track['tracks'])) < 5):
            return []
        else:
            for track in data_top_track['tracks'][:5]:
                ArtistRepository.insert_top_tracks(ArtistRepository.get_uuid(10), uuid_artist, track['name'],
                                                   track['popularity'])
        return (data_artist['name']).casefold()
