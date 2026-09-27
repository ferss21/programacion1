"""Inserta varios tickets y consulta un subconjunto de columnas."""

import sqlite3
from pathlib import Path


ruta = Path(__file__).with_name("tickets.db")
conexion = sqlite3.connect(ruta)
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descripcion TEXT,
        prioridad TEXT,
        estado TEXT
    )
""")
datos = [
    ("Problema de acceso", "No permite iniciar sesión", "Alta", "Abierto"),
    ("Instalar programa", "Instalar editor", "Media", "En proceso"),
]
cursor.executemany(
    "INSERT INTO tickets (titulo, descripcion, prioridad, estado) VALUES (?, ?, ?, ?)",
    datos,
)
conexion.commit()

cursor.execute("SELECT id, titulo, prioridad, estado FROM tickets")
for ticket in cursor.fetchall():
    print(ticket)

print("Abiertos:")
for ticket in cursor.execute(
        "SELECT id, titulo FROM tickets WHERE estado = ?", ("Abierto",)):
    print(ticket)

conexion.close()
