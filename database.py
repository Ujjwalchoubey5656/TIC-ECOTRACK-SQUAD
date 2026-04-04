import sqlite3
from datetime import datetime

def connect():
    return sqlite3.connect("eco_advanced.db", check_same_thread=False)

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS eco_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        co2 REAL,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_record(user, co2):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO eco_logs (user, co2, timestamp)
    VALUES (?, ?, ?)
    """, (user, co2, datetime.now()))

    conn.commit()
    conn.close()

def fetch_records(user):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT co2, timestamp FROM eco_logs
    WHERE user = ?
    ORDER BY id DESC
    """, (user,))

    data = cursor.fetchall()
    conn.close()
    return data
