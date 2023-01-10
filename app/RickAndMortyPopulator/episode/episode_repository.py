import sqlite3 as sql
from config import Config
class EpisodeRepository:
    @staticmethod
    def get_db():
        conn = sql.connect(Config.DATABASE_URI)
        return conn

    @staticmethod
    def create_tables():
        # Las tablas son una lista de sentencias
        tables = [
            """CREATE TABLE IF NOT EXISTS episodes(
            uuid TEXT PRIMARY KEY,
            name TEXT NOT NULL)""",
        ]
        db = EpisodeRepository.get_db()
        cursor = db.cursor()
        for table in tables:
            cursor.execute(table)
    @staticmethod
    def get_one(select,table):
        db = EpisodeRepository.get_db()
        cursor = db.cursor()
        res = cursor.execute("SELECT" + select +"FROM" + table)
        "Return tupla"
        return res.fetchone()

    @staticmethod
    def get_one_where(select, table, where_statement):
        db = EpisodeRepository.get_db()
        cursor = db.cursor()
        res = cursor.execute("SELECT" + select + "FROM" + table + "WHERE" + where_statement)
        "Return tupla"
        return res.fetchone()

    @staticmethod
    def get_all(select, table):
        db = EpisodeRepository.get_db()
        cursor = db.cursor()
        res = cursor.execute("SELECT" + select + "FROM" + table)
        "Return tupla"
        return res.fetchall()

    @staticmethod
    def get_all_order(select, table, order_by):
        db = EpisodeRepository.get_db()
        cursor = db.cursor()
        res = cursor.execute("SELECT" + select + "FROM" + table + "ORDER BY" + order_by)
        "Return tupla"
        return res.fetchall()