import os
from dotenv import load_dotenv

# Carga las variables de entorno en memoria
# Carga todo el contenido de .flaskenv en variables de entorno
load_dotenv()


class Config:
    URL_PORT = 'http://127.0.0.1:9000/'

    DB_PATH_SPOTIFY = "/home/monica/Escritorio/PYTHON_Alberto/baseDeDatos/baseDatos_RickAndMorty _Spotify/app/bbdd_Spotify/db_Spotify.db"
    DB_PATH_RICKANDMORTY = "/home/monica/Escritorio/PYTHON_Alberto/baseDeDatos/baseDatos_RickAndMorty _Spotify/app/bbdd_RickAndMorty/db_RickAndMorty.db"


    URL_Search = 'https://api.spotify.com/v1/search'
    URL_Artist = 'https://api.spotify.com/v1/artists'

    CLIENT_ID = os.environ.get('CLIENT_ID', "")  # O devuelve la variable de entorno o la cadena vacia
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET', "")  # O devuelve la variable de entorno o la cadena vacia