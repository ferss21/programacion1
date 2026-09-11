import sqlite3
from pathlib import Path


RUTA_DB = Path(__file__).with_name("tickets.db")


conexion = sqlite3.connect(RUTA_DB)
cursor = conexion.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        estado TEXT NOT NULL
    )
""")
cursor.execute(
    "INSERT INTO tickets (titulo, estado) VALUES (?, ?)",
    ("Problema de acceso", "Abierto")
)

cursor.execute("SELECT id, titulo, estado FROM tickets")
print("Tickets:")
for ticket in cursor.fetchall():
    print(ticket)

cursor.execute(
    "UPDATE tickets SET estado = ? WHERE id = ?",
    ("Cerrado", 1)
)
cursor.execute("DELETE FROM tickets WHERE id = ?", (1,))
conexion.commit()
conexion.close()
