import sqlite3
from pathlib import Path


ruta = Path(__file__).with_name("notas.db")
conexion = sqlite3.connect(ruta)
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        estudiante TEXT NOT NULL,
        nota REAL NOT NULL
    )
""")
cursor.execute(
    "INSERT INTO notas (estudiante, nota) VALUES (?, ?)",
    ("Estudiante de ejemplo", 85)
)
conexion.commit()

for registro in cursor.execute("SELECT id, estudiante, nota FROM notas"):
    print(registro)

conexion.close()
