from flask import Blueprint

db_RickAndMorty_page = Blueprint('db_RickAndMorty_page', __name__)

@db_RickAndMorty_page.route('/db_RickAndMorty', methods=["GET"])
def index_db():
    return 'Bienvenido a la base de datos de characters de Rick and Morty'
