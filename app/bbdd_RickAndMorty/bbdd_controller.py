from flask import Blueprint
from app.bbdd_RickAndMorty.bbdd_client import SqliteClient

bbdd_page = Blueprint('bbdd_page', __name__)

@bbdd_page.route('/bbdd_RickAndMorty', methods=["GET"])
def index_bbdd():
    return 'Bienvenido a la base de datos de characters de Rick and Morty'
