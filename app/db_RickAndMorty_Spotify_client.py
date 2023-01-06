from app.RickAndMortyPopulator.episode.episode_client import EpisodeClient
from app.RickAndMortyPopulator.character.character_service import RickAndMortyClient
from app.RickAndMortySpotify.artist.artist_topTracks import TopTracks


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
