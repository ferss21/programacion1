"""Inserta tickets y consulta los registros guardados en la nube."""

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
    datos = [
        ("Problema de acceso", "No permite iniciar sesión", "Acceso", "Alta", "Abierto"),
        ("Instalar programa", "Instalar editor", "Software", "Media", "En proceso"),
    ]
    conexion.executemany(
        "INSERT INTO tickets (titulo, descripcion, categoria, prioridad, estado) VALUES (?, ?, ?, ?, ?)",
        datos,
    )
    tickets = conexion.execute(
        "SELECT id, titulo, prioridad, estado FROM tickets"
    ).fetchall()
    abiertos = conexion.execute(
        "SELECT id, titulo FROM tickets WHERE estado = ?", ("Abierto",)
    ).fetchall()

for ticket in tickets:
    print(ticket)

print("Abiertos:")
for ticket in abiertos:
    print(ticket)
