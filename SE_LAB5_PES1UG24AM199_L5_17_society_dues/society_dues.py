"""Manage society maintenance dues and payment status."""
import sqlite3


conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE dues (flat TEXT, month TEXT, amount INTEGER, paid INTEGER)"
)


def add_due(flat, month, amount, history=None):
    """Add a society due and record it in the history."""
    if history is None:
        history = []

    conn.execute(
        "INSERT INTO dues (flat, month, amount, paid) VALUES (?, ?, ?, ?)",
        (flat, month, amount, 0),
    )
    history.append((flat, month))
    return history


def collect(flat, month):
    """Mark a due as paid and return its amount."""
    row = conn.execute(
        "SELECT amount FROM dues WHERE flat = ? AND month = ?",
        (flat, month),
    ).fetchone()

    if row:
        conn.execute(
            "UPDATE dues SET paid = 1 WHERE flat = ? AND month = ?",
            (flat, month),
        )
        return row[0]
    return None


def penalty(base_amount, multiplier):
    """Calculate a late fee using numeric inputs."""
    return base_amount * multiplier


def pending():
    """Return the flats with unpaid dues."""
    rows = conn.execute(
        "SELECT flat FROM dues WHERE paid = 0"
    ).fetchall()
    return [row[0] for row in rows]


def main():
    """Run the society dues demonstration."""
    add_due("A-101", "Oct", 2500)
    add_due("A-102", "Oct", 2500)
    print(collect("A-101", "Oct"))
    print(penalty(50, 2))
    print(pending())


main()
