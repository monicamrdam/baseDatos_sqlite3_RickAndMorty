from flask import Blueprint

bbdd_RickAndMorty_page = Blueprint('bbdd_RickAndMorty_page', __name__)

@bbdd_RickAndMorty_page.route('/bbdd_RickAndMorty', methods=["GET"])
def index_bbdd():
    return 'Bienvenido a la base de datos de characters de Rick and Morty'
