from app import app
from flask import jsonify
from config import Config
from app.bbdd_RickAndMorty.bbdd_client import RickAndMortySqliteClient
from app.bbdd_Spotify.bbdd_Spotify_client import SpotifySqliteClient


@app.route('/')
def home():
    RickAndMortySqliteClient.create_tables()
    SpotifySqliteClient.create_tables()
    message = {
        "Home": Config.URL_PORT,
        "Characters": Config.URL_PORT + 'characters',
        "Episodes": Config.URL_PORT + 'episodes',
        "Artist":Config.URL_PORT + 'artist?name=',
        "BBDD_RickAndMorty": Config.URL_PORT + 'bbdd_RickAndMorty',
        "BBDD_Spotify": Config.URL_PORT + 'bbdd_Spotify',
    }
    return jsonify(message)
