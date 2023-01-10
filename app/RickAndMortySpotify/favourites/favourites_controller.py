from flask import request, Blueprint
from app.RickAndMortySpotify.favourites.favourites_service import FavouritesService

favourite_page = Blueprint('favourite_page', __name__)


@favourite_page.route('/favourites')
def get_favourites():
    return FavouritesService.search_character()
