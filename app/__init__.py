from flask import Flask
from app.character.character_controller import characters_page
from app.bbdd_RickAndMorty.bbdd_controller import bbdd_page
from app.episode.episode_controller import episodes_page
app = Flask(__name__)

app.register_blueprint(characters_page)
app.register_blueprint(episodes_page)
app.register_blueprint(bbdd_page)

from app import routes
