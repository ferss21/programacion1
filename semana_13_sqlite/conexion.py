"""Conexión compartida a SQLite Cloud para los ejemplos de la semana 13."""

from contextlib import contextmanager
import os
from urllib.parse import quote

import sqlitecloud
from dotenv import load_dotenv


load_dotenv()


def conectar():
    """Abre la base remota con host, base y clave guardados en .env."""
    host = os.environ.get("SQLITECLOUD_HOST")
    base = os.environ.get("SQLITECLOUD_DATABASE")
    clave = os.environ.get("SQLITECLOUD_APIKEY")
    if not all((host, base, clave)):
        raise RuntimeError(
            "Configure SQLITECLOUD_HOST, SQLITECLOUD_DATABASE y "
            "SQLITECLOUD_APIKEY en el archivo .env"
        )
    cadena = (
        f"sqlitecloud://{host}:8860/{quote(base, safe='')}"
        f"?apikey={quote(clave, safe='')}"
    )
    return sqlitecloud.connect(cadena)


@contextmanager
def abrir_conexion():
    """Cierra la conexión y guarda los cambios al terminar sin errores."""
    conexion = conectar()
    try:
        yield conexion
        conexion.commit()
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()
