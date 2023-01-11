import random
from app.RickAndMortyPopulator.character.character_repository import CharacterRepository
from app.RickAndMortySpotify.artist.artist_service import SpotifyService


class FavouritesService:
    @staticmethod
    def search_character():
        db = CharacterRepository.get_db()
        cursor = db.cursor()
        res = cursor.execute("SELECT name FROM characters")
        "Return tupla"
        all_characters = res.fetchall()
        rd_num = (random.randrange(len(all_characters)))
        rd_name =''.join(all_characters[rd_num])
        #name =''.join(rd_name.split())
        print(rd_name)
        return SpotifyService.result_search(rd_name)
