import sqlite3 as sql

class SqliteClient:

    @staticmethod
    def get_bbdd():
        conn = sql.connect('bbdd_RickAndMorty.db')
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
        db = SqliteClient.get_bbdd()
        cursor = db.cursor()
        for table in tables:
            cursor.execute(table)