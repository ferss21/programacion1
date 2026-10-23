# Semana 13: SQLite en la nube

## Objetivo

Guardar datos de forma persistente y conectarse desde Python a una base SQLite disponible por internet.

## Temas

Tablas, conexión, CRUD, consultas parametrizadas y el controlador `sqlitecloud`, compatible con la interfaz de `sqlite3` para conectarse a SQLite Cloud.

## Ejecutar y practicar

Los ejemplos y el CRUD se conectan a una misma base remota de SQLite Cloud. El archivo `conexion.py` centraliza esa conexión y carga los valores de `.env`. El controlador `sqlitecloud` conserva la forma de trabajo de `sqlite3` y permite usar los parámetros `?` en las consultas.

## Crear una base en SQLite Cloud

1. Regístrese en [SQLite Cloud](https://dashboard.sqlitecloud.io/) y cree un proyecto.
2. Desde el panel, cree una base de datos para las solicitudes y abra **Show connection strings**.
3. Copie `.env.example` como `.env` y complete los tres valores: host, nombre de base y clave de API. Use el host de la cadena de conexión para el SDK de Python; escriba solo el dominio, sin `https://`. No comparta ni suba su `.env`.
4. Instale los paquetes desde esta carpeta con `python -m pip install -r requirements.txt`.
5. Ejecute `python validar_conexion.py`. Si muestra que la conexión es correcta, ejecute `python ejemplo_01_crear.py`; después puede probar los otros ejemplos y `practica.py`.

Al ejecutar el ejemplo 1, la tabla se crea en la base elegida en el panel. Los siguientes programas se conectan a esa misma base por internet; no crean un archivo `.db` en la computadora. `conexion.py` carga `.env` y construye una cadena con formato `sqlitecloud://HOST:8860/BASE?apikey=CLAVE`. El archivo `.env` está excluido de Git.

La aplicación puede crear esta tabla al iniciar:

```sql
CREATE TABLE IF NOT EXISTS solicitudes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    categoria TEXT NOT NULL,
    prioridad TEXT NOT NULL,
    estado TEXT NOT NULL
);
```

Consulte la [introducción oficial al SDK de Python](https://docs.sqlitecloud.io/docs/sdk-python-introduction) y el [plan gratuito](https://sqlitecloud.io/pricing), que incluye límites de uso sujetos a cambios. Guarde las credenciales fuera del código y no las suba al repositorio.

## Actividades

- [Actividad de clase](actividad_clase.md): CRUD de solicitudes en SQLite Cloud.
- [Práctica guiada](practica_sqlite_cloud.py): ejercicio para completar la conexión y CRUD en la nube.
- [Conexión compartida](conexion.py): lee la configuración y administra el cierre de cada sesión.
- [Validador de conexión](validar_conexion.py): comprueba el acceso sin mostrar la clave.
- [CRUD de ejemplo](practica.py): aplicación completa de consola sobre la misma cuenta de SQLite Cloud.
- [Tarea evaluada](tarea_evaluada.md): sistema persistente conectado a SQLite en la nube.
