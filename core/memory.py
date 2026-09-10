import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "venus.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_memory():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE NOT NULL,
            value TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def remember(key, value):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO memory (key, value)
        VALUES (?, ?)
        ON CONFLICT(key)
        DO UPDATE SET value = excluded.value
    """, (key, value))

    connection.commit()
    connection.close()


def recall(key):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT value FROM memory WHERE key = ?",
        (key,)
    )

    result = cursor.fetchone()

    connection.close()

    if result:
        return result[0]

    return None


def forget(key):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM memory WHERE key = ?",
        (key,)
    )

    connection.commit()
    connection.close()


def get_all_memory():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT key, value FROM memory")

    memories = cursor.fetchall()

    connection.close()

    return memories