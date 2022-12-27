from flask import Flask
from app.character.character_controller import characters_page
from app.episode.episode_controller import episodes_page
from app.artist.artist_controller import artist_page
from app.bbdd_RickAndMorty.bbdd_RickMorty_controller import db_RickAndMorty_page
from app.bbdd_Spotify.bbdd_Spotify_controller import db_Spotify_page

app = Flask(__name__)

app.register_blueprint(characters_page)
app.register_blueprint(episodes_page)
app.register_blueprint(artist_page)
app.register_blueprint(db_RickAndMorty_page)
app.register_blueprint(db_Spotify_page)

from app import routes
