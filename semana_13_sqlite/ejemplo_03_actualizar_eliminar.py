"""Actualiza y elimina tickets con consultas parametrizadas en la nube."""

from conexion import abrir_conexion


id_ticket = int(input("Id del ticket: "))
nuevo_estado = input("Nuevo estado: ")

with abrir_conexion() as conexion:
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            categoria TEXT NOT NULL,
            prioridad TEXT,
            estado TEXT
        )
    """)
    resultado = conexion.execute(
        "UPDATE tickets SET estado = ? WHERE id = ?",
        (nuevo_estado, id_ticket),
    )
    print("Registros actualizados:", resultado.rowcount)

    if input("¿Desea eliminar este ticket? (s/n): ").lower() == "s":
        resultado = conexion.execute(
            "DELETE FROM tickets WHERE id = ?", (id_ticket,)
        )
        print("Registros eliminados:", resultado.rowcount)

print("Cambios guardados")
