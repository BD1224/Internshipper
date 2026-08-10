import sqlite3  # built in SQL system
from config import DB_PATH

def init_db():
    conn = sqlite3.connect(DB_PATH)  # holds sql connected to file
    cursor = conn.cursor()  # used to run sql commands

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            found_application BOOLEAN NOT NULL DEFAULT 0,
            includes_global_words BOOLEAN NOT NULL DEFAULT 1
        )
    """)  # creates table if doesnt already exist

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS site_words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site_id INTEGER,
            word TEXT NOT NULL,
            is_global BOOLEAN NOT NULL DEFAULT 1
        )
    """)  # creates words table
    # site_id can be null, if its a global word

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)  # table for single variables

    cursor.execute(
        "INSERT INTO settings (key, value) VALUES (?, ?)",
        ("prev_print", "")
    )  # starts tracking the previous print

    conn.commit()  # save
    conn.close()

    print("Database initialized")

if __name__ == "__main__":
    init_db()