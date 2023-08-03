import sqlite3


class Entry:
    def __init__(self, id, date, content):
        self.id = id
        self.date = date
        self.content = content
        super().__init__()

    @staticmethod
    def create(date, content):
        with sqlite3.connect("db.sqlite3") as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO entries (date, content) VALUES (?, ?) RETURNING id, date, content",
                (date, content),
            )
            row = cursor.fetchone()
            return Entry(row[0], row[1], row[2])

    @staticmethod
    def all():
        with sqlite3.connect("db.sqlite3") as conn:
            cursor = conn.execute("SELECT * FROM entries")
            return [Entry(row[0], row[1], row[2]) for row in cursor.fetchall()]

    def __str__(self):
        return f"\n{self.date}\n{self.content}"
