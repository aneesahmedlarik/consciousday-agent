# SQLite logic for insert, fetch, and table creation
import sqlite3

def init_db():
    conn = sqlite3.connect("entries.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            journal TEXT,
            intention TEXT,
            dream TEXT,
            priorities TEXT,
            reflection TEXT,
            strategy TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_entry(date, journal, dream, intention, priorities, output):
    conn = sqlite3.connect("entries.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO entries (date, journal, intention, dream, priorities, reflection, strategy)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (date, journal, intention, dream, priorities, output, output))
    conn.commit()
    conn.close()

def fetch_entry_by_date(date):
    conn = sqlite3.connect("entries.db")
    c = conn.cursor()
    c.execute("SELECT reflection, strategy FROM entries WHERE date = ?", (date,))
    row = c.fetchone()
    conn.close()
    if row:
        return row[0]  # Returning the combined output
    return None
