from flask import request, Blueprint
from app.RickAndMortySpotify.artist.artist_service import SpotifyService

favourite_page = Blueprint('favourite_page', __name__)


@favourite_page.route('/favourites')
def get_favourites():
    return 'Pendiente de crear'