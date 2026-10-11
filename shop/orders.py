"""Order queries over the shop database."""

import sqlite3

_SCHEMA = """
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    total_cents INTEGER NOT NULL,
    status TEXT NOT NULL
);
INSERT INTO orders (id, customer_id, total_cents, status) VALUES
    (1001, 1, 4999, 'paid'),
    (1002, 2, 1250, 'paid'),
    (1003, 1, 800, 'refunded');
"""


def connect():
    """Open the shop database (in-memory for the demo) with its seed data."""
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    conn.executescript(_SCHEMA)
    return conn


def list_orders(conn, status=None):
    """Orders as (id, customer_id, total_cents, status) rows, optionally filtered by status."""
    if status is None:
        cursor = conn.execute("SELECT id, customer_id, total_cents, status FROM orders ORDER BY id")
    else:
        cursor = conn.execute(
            "SELECT id, customer_id, total_cents, status FROM orders WHERE status = ? ORDER BY id",
            (status,),
        )
    return cursor.fetchall()
