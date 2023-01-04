from app import app
from flask import jsonify
from config import Config
from app.db_RickAndMorty_Spotify_client import Db_RickAndMorty_Spotify


@app.route('/')
def home():
    Db_RickAndMorty_Spotify.create_table_characters()
    Db_RickAndMorty_Spotify.create_table_episode()
    Db_RickAndMorty_Spotify.create_table_artist()
    message = {
        "Home": Config.URL_PORT,
        "Characters": Config.URL_PORT + 'characters',
        "Episodes": Config.URL_PORT + 'episodes',
        "Artist":Config.URL_PORT + 'artist?name=',
    }
    return jsonify(message)
