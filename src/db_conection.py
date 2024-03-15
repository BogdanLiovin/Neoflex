import sqlite3

class DBConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.conn = sqlite3.connect('my_db.db')  # Имя базы данных SQLite
        return cls._instance

    def save_to_db(self, sql_query):
        cursor = self.conn.cursor()
        cursor.execute(sql_query)
        self.conn.commit()

    def execute_scalar(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        result = cursor.fetchone()[0]
        return result

    @staticmethod
    def getInstance():
        return DBConnection()