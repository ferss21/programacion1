"""Punto de partida para conectar el proyecto con SQLite Cloud."""

import os

import sqlitecloud


def conectar():
    """Abre una conexión usando SQLITECLOUD_URL del entorno."""
    cadena = os.environ.get("SQLITECLOUD_URL")
    if not cadena:
        raise RuntimeError("Configure la variable de entorno SQLITECLOUD_URL")
    return sqlitecloud.connect(cadena)


def crear_tabla():
    """Crea la tabla inicial; complete aquí el esquema acordado."""
    conexion = conectar()
    try:
        conexion.execute("""
            CREATE TABLE IF NOT EXISTS solicitudes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                categoria TEXT NOT NULL,
                prioridad TEXT NOT NULL,
                estado TEXT NOT NULL,
                reportado_por TEXT NOT NULL
            )
        """)
        conexion.commit()
    finally:
        conexion.close()


# Complete aquí las operaciones parametrizadas para crear, consultar,
# actualizar y eliminar solicitudes.
