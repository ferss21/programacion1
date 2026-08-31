import sqlite3
from pathlib import Path


RUTA_DB = Path(__file__).with_name("tickets.db")


def conectar():
    return sqlite3.connect(RUTA_DB)


def crear_tabla():
    conexion = conectar()
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            categoria TEXT,
            prioridad TEXT,
            estado TEXT
        )
    """)
    conexion.commit()
    conexion.close()


# Faltan las funciones para insertar, consultar, actualizar y eliminar.
