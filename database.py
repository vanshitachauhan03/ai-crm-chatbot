import sqlite3

def create_db():
    conn = sqlite3.connect("crm.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers(
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        issue TEXT
    )
    """)

    conn.commit()
    conn.close()
