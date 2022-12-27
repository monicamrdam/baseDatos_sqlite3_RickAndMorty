from flask import Blueprint

bbdd_Spotify_page = Blueprint('bbdd_Spotify_page', __name__)

@bbdd_Spotify_page.route('/bbdd_Spotify', methods=["GET"])
def index_bbdd():
    return 'Bienvenido a la base de datos de artist de Spotify'
