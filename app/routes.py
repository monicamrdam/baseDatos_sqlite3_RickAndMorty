from app import app
from flask import jsonify
from config import Config
from app.bbdd_RickAndMorty.bbdd_client import SqliteClient


@app.route('/')
def home():
    SqliteClient.create_tables()
    message = {
        "Home": Config.URL_PORT,
        "Characters": Config.URL_PORT + 'characters',
        "Episodes": Config.URL_PORT + 'episodes',
        "BBDD": Config.URL_PORT + 'bbdd_RickAndMorty',
    }
    return jsonify(message)
