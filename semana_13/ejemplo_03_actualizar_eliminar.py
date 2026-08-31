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

if input("¿Desea eliminar este ticket? (s/n): ").lower() == "s":
    cursor.execute("DELETE FROM tickets WHERE id = ?", (id_ticket,))

conexion.commit()
conexion.close()
print("Cambios guardados")
