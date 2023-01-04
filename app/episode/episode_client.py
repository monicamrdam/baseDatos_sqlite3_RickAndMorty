import requests
import sqlite3 as sql
from config import Config

class EpisodeClient:
    def __init__(self):
        pass

    @staticmethod
    def base_url():
        return 'https://rickandmortyapi.com/api/'

    @staticmethod
    def end_point_episode():
        return 'episode'

    @staticmethod
    def main_path(baseurl, endpoint):
        r = requests.get(baseurl + endpoint)
        return r.json()

    @staticmethod
    def get_db():
        conn = sql.connect(Config.DATABASE_URI)
        return conn

    @staticmethod
    def create_tables():
        # Las tablas son una lista de sentencias
        tables = [
            """CREATE TABLE IF NOT EXISTS episodes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL)""",
        ]
        db = EpisodeClient.get_db()
        cursor = db.cursor()
        for table in tables:
            cursor.execute(table)