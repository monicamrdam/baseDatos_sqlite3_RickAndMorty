from app.episode.episode_client import EpisodeClient
from app.character.rick_and_morty_client import RickAndMortyClient
from app.artist.artist_topTracks import TopTracks


class Db_RickAndMorty_Spotify:

    @staticmethod
    def create_table_characters():
        RickAndMortyClient.create_tables()

    @staticmethod
    def create_table_episode():
        EpisodeClient.create_tables()

    @staticmethod
    def create_table_artist():
        TopTracks.create_tables()
