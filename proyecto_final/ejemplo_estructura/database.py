"""Punto de partida para encapsular la persistencia del proyecto final."""

import sqlite3
from pathlib import Path


RUTA_DB = Path(__file__).with_name("tickets.db")


def conectar():
    """Devuelve una conexión a la base local del proyecto."""
    return sqlite3.connect(RUTA_DB)


def crear_tabla():
    """Crea el esquema si todavía no existe."""
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


# El estudiante debe completar aquí insertar, consultar, actualizar y eliminar.
