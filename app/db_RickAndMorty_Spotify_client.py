from app.RickAndMortyPopulator.episode.episode_repository import EpisodeRepository
from app.RickAndMortyPopulator.character.character_repository import CharacterRepository
from app.RickAndMortySpotify.artist.artist_repository import ArtistRepository


class DbRickAndMortySpotify:

    @staticmethod
    def create_table_characters():
        CharacterRepository.create_tables()

    @staticmethod
    def create_table_episode():
        EpisodeRepository.create_tables()

    @staticmethod
    def create_table_artist():
        ArtistRepository.create_tables()
