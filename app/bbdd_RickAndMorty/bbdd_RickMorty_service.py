from app.bbdd_RickAndMorty.bbdd_RickMorty_client import RickAndMortySqliteClient


class SqliteService:
    @staticmethod
    def insert_character(name, location):
        db = RickAndMortySqliteClient.get_db()
        cursor = db.cursor()
        statement = "INSERT INTO characters (name, location) VALUES (?,?)"
        cursor.execute(statement, [name, location])
        db.commit()

    @staticmethod
    def insert_episode(name):
        db = RickAndMortySqliteClient.get_db()
        cursor = db.cursor()
        statement = "INSERT INTO episodes (name) VALUES (?)"
        cursor.execute(statement, [name])
        db.commit()