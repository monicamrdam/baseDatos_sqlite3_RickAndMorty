import os
from dotenv import load_dotenv

# Carga las variables de entorno en memoria
# Carga todo el contenido de .flaskenv en variables de entorno
load_dotenv()


class Config:
    URL_PORT = 'http://127.0.0.1:9000/'

    DB_PATH = "/home/monica/Escritorio/PYTHON_Alberto/baseDeDatos/base_de_datos_sqlite3_copia_copia/app/rest_api_sql/rest_api.db"

    URL_Search = 'https://api.spotify.com/v1/search'
    URL_Artist = 'https://api.spotify.com/v1/artists'

    CLIENT_ID = os.environ.get('CLIENT_ID', "")  # O devuelve la variable de entorno o la cadena vacia
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET', "")  # O devuelve la variable de entorno o la cadena vacia