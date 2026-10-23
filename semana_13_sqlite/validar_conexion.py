"""Comprueba la conexión a SQLite Cloud sin mostrar la clave."""

from conexion import abrir_conexion


try:
    with abrir_conexion() as conexion:
        version = conexion.execute("SELECT sqlite_version()").fetchone()[0]
except Exception:
    print("No fue posible conectar. Revise el host, el nombre de la base y la clave en .env.")
else:
    print("Conexión correcta a SQLite Cloud.")
    print("Versión de SQLite:", version)

