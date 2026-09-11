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

conexion.commit()
conexion.close()
print("Tabla creada")
