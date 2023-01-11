import sqlite3 as sql
import random, string
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
            popularity INTEGER NOT NULL)""",

            """CREATE TABLE IF NOT EXISTS top_artist(
            uuid TEXT PRIMARY KEY,
            uuid_artist TEXT NOT NULL,
            name_song TEXT NOT NULL,
            popularity_song TEXT NOT NULL)""",
        ]
        db = ArtistRepository.get_db()
        cursor = db.cursor()
        for table in tables:
            cursor.execute(table)

    @staticmethod
    def get_uuid(num_dig):
        uuid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num_dig))
        return uuid
    @staticmethod
    def insert_artist(uuid,name,popularity):
        db = ArtistRepository.get_db()
        cursor = db.cursor()
        statement = "INSERT INTO artist (uuid, name, popularity) VALUES (?,?,?)"
        cursor.execute(statement, [uuid,name,popularity])
        db.commit()

    @staticmethod
    def insert_top_tracks(uuid, uuid_artist, name_song,popularity_song ):
        db = ArtistRepository.get_db()
        cursor = db.cursor()
        statement = "INSERT INTO top_artist (uuid, uuid_artist, name_song,popularity_song ) VALUES (?,?,?,?)"
        cursor.execute(statement, [uuid, uuid_artist, name_song,popularity_song])
        db.commit()

    @staticmethod
    def get_one_where_name_artist(name):
        db = ArtistRepository.get_db()
        cursor = db.cursor()
        res = cursor.execute("SELECT * FROM artist WHERE name='" + name +"'")
        return res