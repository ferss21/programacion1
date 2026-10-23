"""Crea la tabla tickets en la base remota de SQLite Cloud."""

from conexion import abrir_conexion


with abrir_conexion() as conexion:
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            categoria TEXT NOT NULL,
            prioridad TEXT,
            estado TEXT
        )
    """)

print("Tabla creada en SQLite Cloud")
