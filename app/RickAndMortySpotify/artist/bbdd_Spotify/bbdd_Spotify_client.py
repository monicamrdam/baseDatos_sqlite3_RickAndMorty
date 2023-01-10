import sqlite3 as sql
from config import Config

class SpotifySqliteClient:

    @staticmethod
    def get_db():
        conn = sql.connect(Config.DB_PATH_SPOTIFY)
        return conn

    @staticmethod
    def create_tables():
        # Las tablas son una lista de sentencias
        tables = [
            """CREATE TABLE IF NOT EXISTS artist(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            uri_artist TEXT NOT NULL,
            name_artist TEXT NOT NULL,
            popularity INTEGER NOT NULL)""",

            """CREATE TABLE IF NOT EXISTS top_artist(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name_artist TEXT NOT NULL,
            name_song TEXT NOT NULL,
            popularity_song TEXT NOT NULL)""",
        ]
        db = SpotifySqliteClient.get_db()
        cursor = db.cursor()
        for table in tables:
            cursor.execute(table)