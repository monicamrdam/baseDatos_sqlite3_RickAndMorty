from flask import Blueprint
from app.character.character_service import RickAndMortyService
from app.character.rick_and_morty_client import RickAndMortyClient

characters_page = Blueprint('characters_page', __name__)

@characters_page.route('/characters')
def get_characters():
    return RickAndMortyService.data_character(RickAndMortyClient.base_url(), RickAndMortyClient.end_point_character())

