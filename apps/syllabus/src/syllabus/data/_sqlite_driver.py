import sqlite3
import pandas as pd

from syllabus.ports.dbs import DatabasePort


class SQLiteDriver(DatabasePort):
    def __init__(self, db_path) -> None:
        self.db_path = db_path
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
            print(f"Connected to SQLite database at {self.db_path}")
        except sqlite3.Error as e:
            print(f"Error connecting to SQLite database: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from SQLite database")

    def query(self, query: str):
        if not self.connection:
            raise ConnectionError("Database is not connected")
        df = pd.read_sql_query(query, self.connection)
        return df