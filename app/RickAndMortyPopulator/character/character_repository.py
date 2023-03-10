import sqlite3 as sql
from config import Config
class CharacterRepository:
    @staticmethod
    def get_db():
        conn = sql.connect(Config.DATABASE_URI)
        return conn

    @staticmethod
    def create_tables():
        # Las tablas son una lista de sentencias
        tables = [
            """CREATE TABLE IF NOT EXISTS characters(
            uuid TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            location TEXT NOT NULL)""",
        ]
        db = CharacterRepository.get_db()
        cursor = db.cursor()
        for table in tables:
            cursor.execute(table)