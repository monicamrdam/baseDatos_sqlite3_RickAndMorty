import sqlite3 as sql
from config import Config

class RickAndMortySqliteClient:

    @staticmethod
    def get_db():
        conn = sql.connect(Config.DB_PATH_RICKANDMORTY)
        return conn

    @staticmethod
    def create_tables():
        # Las tablas son una lista de sentencias
        tables = [
            """CREATE TABLE IF NOT EXISTS characters(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL)""",

            """CREATE TABLE IF NOT EXISTS episodes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL)""",
        ]
        db = RickAndMortySqliteClient.get_db()
        cursor = db.cursor()
        for table in tables:
            cursor.execute(table)