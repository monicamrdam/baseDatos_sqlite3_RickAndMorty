import sqlite3 as sql
from config import Config
class ArtistRepository:
    @staticmethod
    def get_db():
        conn = sql.connect(Config.DATABASE_URI)
        return conn

    @staticmethod
    def create_tables():
        # Las tablas son una lista de sentencias
        tables = [
            """CREATE TABLE IF NOT EXISTS artist(
            uuid TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            location TEXT NOT NULL)""",
        ]
        db = ArtistRepository.get_db()
        cursor = db.cursor()
        for table in tables:
            cursor.execute(table)