"""Actualiza y elimina un ticket usando consultas parametrizadas."""

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

id_ticket = int(input("Id del ticket: "))
nuevo_estado = input("Nuevo estado: ")
cursor.execute(
    "UPDATE tickets SET estado = ? WHERE id = ?",
    (nuevo_estado, id_ticket)
)
print("Registros actualizados:", cursor.rowcount)

if input("¿Desea eliminar este ticket? (s/n): ").lower() == "s":
    cursor.execute("DELETE FROM tickets WHERE id = ?", (id_ticket,))
    print("Registros eliminados:", cursor.rowcount)

conexion.commit()
conexion.close()
print("Cambios guardados")
