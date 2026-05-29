import sqlite3
from datetime import datetime


def init_database():
    connection = sqlite3.connect("loan_calculations.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS loan_calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            principal REAL NOT NULL,
            annual_rate REAL NOT NULL,
            months INTEGER NOT NULL,
            monthly_payment REAL NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_loan_calculation(
    principal,
    annual_rate,
    months,
    monthly_payment
):
    connection = sqlite3.connect("loan_calculations.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO loan_calculations
        (
            principal,
            annual_rate,
            months,
            monthly_payment,
            created_at
        )
        VALUES (?, ?, ?, ?, ?)
    """,
    (
        principal,
        annual_rate,
        months,
        monthly_payment,
        datetime.utcnow().isoformat()
    ))

    connection.commit()
    connection.close()