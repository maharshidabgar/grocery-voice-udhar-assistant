import sqlite3
from config import DATABASE_PATH


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.connection.cursor()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetchone(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

def create_tables():

    db = Database()

    db.execute("""

    CREATE TABLE IF NOT EXISTS customers(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        mobile TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    db.execute("""

    CREATE TABLE IF NOT EXISTS aliases(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        customer_id INTEGER,

        alias TEXT UNIQUE,

        FOREIGN KEY(customer_id) REFERENCES customers(id)

    )

    """)

    db.execute("""

    CREATE TABLE IF NOT EXISTS transactions(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        customer_id INTEGER,

        type TEXT,

        amount REAL,

        note TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(customer_id) REFERENCES customers(id)

    )

    """)

    db.close()