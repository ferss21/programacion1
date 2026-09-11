import sqlite3
from pathlib import Path


ruta = Path(__file__).with_name("practica_tickets.db")


def conectar():
    return sqlite3.connect(ruta)


def crear_tabla():
    conexion = conectar()
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            estado TEXT NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()


def agregar():
    titulo = input("Título: ")
    conexion = conectar()
    conexion.execute(
        "INSERT INTO tickets (titulo, estado) VALUES (?, ?)",
        (titulo, "Abierto")
    )
    conexion.commit()
    conexion.close()


def mostrar():
    conexion = conectar()
    tickets = conexion.execute("SELECT id, titulo, estado FROM tickets").fetchall()
    conexion.close()
    for ticket in tickets:
        print(ticket)


def actualizar():
    id_ticket = int(input("Id: "))
    estado = input("Nuevo estado: ")
    conexion = conectar()
    conexion.execute("UPDATE tickets SET estado = ? WHERE id = ?", (estado, id_ticket))
    conexion.commit()
    conexion.close()


def eliminar():
    id_ticket = int(input("Id: "))
    conexion = conectar()
    conexion.execute("DELETE FROM tickets WHERE id = ?", (id_ticket,))
    conexion.commit()
    conexion.close()


crear_tabla()
opcion = ""
while opcion != "5":
    print("\n1. Crear  2. Consultar  3. Actualizar  4. Eliminar  5. Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        agregar()
    elif opcion == "2":
        mostrar()
    elif opcion == "3":
        actualizar()
    elif opcion == "4":
        eliminar()
    elif opcion != "5":
        print("Opción no válida")
