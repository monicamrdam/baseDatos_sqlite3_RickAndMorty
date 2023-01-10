from app import app
from flask import jsonify
from config import Config
from app.db_RickAndMorty_Spotify_client import DbRickAndMortySpotify


@app.route('/')
def home():
    DbRickAndMortySpotify.create_table_characters()
    DbRickAndMortySpotify.create_table_episode()
    DbRickAndMortySpotify.create_table_artist()
    message = {
        "Home": Config.URL_PORT,
        "Characters": Config.URL_PORT + 'characters',
        "Episodes": Config.URL_PORT + 'episodes',
        "Artist": Config.URL_PORT + 'artist?name=',
        "Favourites": Config.URL_PORT + 'favourites',
    }
    return jsonify(message)
