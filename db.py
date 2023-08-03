import sqlite3


def init_db():
    conn = sqlite3.connect("db.sqlite3")
    conn.execute(
        "CREATE TABLE IF NOT EXISTS entries (id INTEGER NOT NULL PRIMARY KEY, date TEXT, content TEXT);"
    )
    conn.close()
