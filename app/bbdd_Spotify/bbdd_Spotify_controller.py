from flask import Blueprint

db_Spotify_page = Blueprint('db_Spotify_page', __name__)

@db_Spotify_page.route('/db_Spotify', methods=["GET"])
def index_db():
    return 'Bienvenido a la base de datos de artist de Spotify'
