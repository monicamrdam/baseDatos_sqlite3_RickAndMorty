from flask import Blueprint
from app.RickAndMortyPopulator.character.character_service import RickAndMortyService
from app.RickAndMortyPopulator.character.character_service import RickAndMortyClient

characters_page = Blueprint('characters_page', __name__)

@characters_page.route('/characters')
def get_characters():
    return RickAndMortyService.data_character(RickAndMortyClient.base_url(), RickAndMortyClient.end_point_character())

