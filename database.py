import sqlite3

def init_db():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        note TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_note(user_id, note):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (user_id, note) VALUES (?, ?)", (user_id, note))
    conn.commit()
    conn.close()

def get_notes(user_id):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, note FROM notes WHERE user_id = ?", (user_id,))
    notes = cursor.fetchall()
    conn.close()
    return notes

def delete_note(note_id):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
