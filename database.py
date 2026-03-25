import sqlite3

def save_result(score):
    conn = sqlite3.connect("interview.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        score INTEGER
    )
    """)

    cursor.execute("INSERT INTO results VALUES (?)", (score,))
    conn.commit()
    conn.close()