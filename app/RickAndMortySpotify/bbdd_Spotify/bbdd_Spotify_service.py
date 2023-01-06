from app.RickAndMortySpotify.bbdd_Spotify.bbdd_Spotify_client import SpotifySqliteClient


class SqliteService:
    @staticmethod
    def insert_artist(uri_artist, name_artist, popularity):
        db = SpotifySqliteClient.get_db()
        cursor = db.cursor()
        statement = "INSERT INTO artist (uri_artist, name_artist,popularity) VALUES (?,?,?)"
        cursor.execute(statement, [uri_artist, name_artist, popularity])
        db.commit()

    @staticmethod
    def insert_top_artist(name_artist, name_song, popularity_song):
        db = SpotifySqliteClient.get_db()
        cursor = db.cursor()
        statement = "INSERT INTO top_artist (name_artist, name_song, popularity_song) VALUES (?,?,?)"
        cursor.execute(statement, [name_artist, name_song, popularity_song])
        db.commit()
