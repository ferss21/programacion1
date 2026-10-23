"""CRUD de tickets con SQLite Cloud, validaciones y funciones separadas."""

from conexion import abrir_conexion

ESTADOS = ("Abierto", "En proceso", "Cerrado")
PRIORIDADES = ("Baja", "Media", "Alta")


def crear_tabla():
    with abrir_conexion() as conexion:
        conexion.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                categoria TEXT NOT NULL,
                prioridad TEXT NOT NULL,
                estado TEXT NOT NULL
            )
        """)


def agregar():
    datos = (
        input("Título: ").strip(),
        input("Descripción: ").strip(),
        input("Categoría: ").strip(),
        input("Prioridad (Baja/Media/Alta): ").strip().title(),
        "Abierto",
    )
    if not datos[0] or not datos[1] or datos[3] not in PRIORIDADES:
        print("Título, descripción y prioridad son obligatorios")
        return
    with abrir_conexion() as conexion:
        conexion.execute(
            """INSERT INTO tickets
            (titulo, descripcion, categoria, prioridad, estado)
            VALUES (?, ?, ?, ?, ?)""",
            datos,
        )
    print("Ticket creado")


def mostrar():
    with abrir_conexion() as conexion:
        tickets = conexion.execute(
            """SELECT id, titulo, categoria, prioridad, estado
            FROM tickets ORDER BY id"""
        ).fetchall()
    if not tickets:
        print("No hay tickets")
    for ticket in tickets:
        print(ticket)


def buscar():
    texto = input("Texto a buscar: ").strip()
    with abrir_conexion() as conexion:
        tickets = conexion.execute(
            """SELECT id, titulo, prioridad, estado FROM tickets
            WHERE titulo LIKE ? OR descripcion LIKE ?""",
            (f"%{texto}%", f"%{texto}%"),
        ).fetchall()
    for ticket in tickets:
        print(ticket)
    if not tickets:
        print("No se encontraron coincidencias")


def actualizar():
    id_ticket = int(input("Id: "))
    estados = {valor.casefold(): valor for valor in ESTADOS}
    estado = estados.get(input("Nuevo estado (Abierto/En proceso/Cerrado): ").strip().casefold())
    if estado is None:
        print("Estado no válido")
        return
    with abrir_conexion() as conexion:
        resultado = conexion.execute(
            "UPDATE tickets SET estado = ? WHERE id = ?", (estado, id_ticket)
        )
        print("Registros actualizados:", resultado.rowcount)


def eliminar():
    id_ticket = int(input("Id: "))
    with abrir_conexion() as conexion:
        resultado = conexion.execute("DELETE FROM tickets WHERE id = ?", (id_ticket,))
        print("Registros eliminados:", resultado.rowcount)


crear_tabla()
opcion = ""
while opcion != "6":
    print("\n1. Crear  2. Consultar  3. Buscar  4. Actualizar  5. Eliminar  6. Salir")
    opcion = input("Opción: ").strip()
    if opcion == "1":
        agregar()
    elif opcion == "2":
        mostrar()
    elif opcion == "3":
        buscar()
    elif opcion == "4":
        actualizar()
    elif opcion == "5":
        eliminar()
    elif opcion != "6":
        print("Opción no válida")
