from flask import request, Blueprint
from app.RickAndMortySpotify.artist.artist_service import SpotifyService

artist_page = Blueprint('artist_page', __name__)


@artist_page.route('/artist')
def spotify_service():
    name = request.args.get('name', type=str)
    return SpotifyService.result_search(name)
