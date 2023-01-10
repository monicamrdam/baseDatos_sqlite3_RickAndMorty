from flask import Flask
from app.RickAndMortyPopulator.character.character_controller import characters_page
from app.RickAndMortyPopulator.episode.episode_controller import episodes_page
from app.RickAndMortySpotify.artist.artist_controller import artist_page
from app.RickAndMortySpotify.favourites.favourites_controller import favourite_page

app = Flask(__name__)

app.register_blueprint(characters_page)
app.register_blueprint(episodes_page)
app.register_blueprint(artist_page)
app.register_blueprint(favourite_page)

from app import routes
