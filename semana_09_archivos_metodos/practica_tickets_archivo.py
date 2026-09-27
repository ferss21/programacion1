"""CRUD sencillo de tickets almacenado en un archivo delimitado."""

from pathlib import Path


RUTA = Path(__file__).with_name("tickets.txt")
SEPARADOR = "|"


def cargar_tickets():
    """Convierte las líneas existentes en una lista de diccionarios."""
    RUTA.touch(exist_ok=True)
    tickets = []
    with open(RUTA, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = [parte.strip() for parte in linea.split(SEPARADOR)]
            if len(partes) == 4 and all(partes):
                codigo, titulo, prioridad, estado = partes
                tickets.append({
                    "codigo": codigo,
                    "titulo": titulo,
                    "prioridad": prioridad,
                    "estado": estado,
                })
    return tickets


def guardar_tickets(tickets):
    """Reescribe el archivo para conservar altas, cambios y eliminaciones."""
    with open(RUTA, "w", encoding="utf-8") as archivo:
        for ticket in tickets:
            datos = [ticket["codigo"], ticket["titulo"], ticket["prioridad"], ticket["estado"]]
            archivo.write(f" {SEPARADOR} ".join(datos) + "\n")


def mostrar(tickets):
    """Muestra tickets o informa cuando no hay registros."""
    if not tickets:
        print("No hay tickets")
        return
    for ticket in tickets:
        print(ticket["codigo"], "-", ticket["titulo"], "-", ticket["prioridad"], "-", ticket["estado"])


tickets = cargar_tickets()
opcion = ""
while opcion != "6":
    print("\n1. Registrar  2. Listar  3. Buscar  4. Actualizar  5. Eliminar  6. Salir")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        ticket = {
            "codigo": input("Código: ").strip().upper(),
            "titulo": input("Título: ").strip(),
            "prioridad": input("Prioridad: ").strip().title(),
            "estado": "Abierto",
        }
        tickets.append(ticket)
        guardar_tickets(tickets)
        print("Ticket guardado")
    elif opcion == "2":
        mostrar(tickets)
    elif opcion in ("3", "4", "5"):
        codigo = input("Código: ").strip().upper()
        encontrado = next((ticket for ticket in tickets if ticket["codigo"] == codigo), None)
        if encontrado is None:
            print("Ticket no encontrado")
        elif opcion == "3":
            mostrar([encontrado])
        elif opcion == "4":
            encontrado["estado"] = input("Nuevo estado: ").strip().title()
            guardar_tickets(tickets)
            print("Ticket actualizado")
        else:
            tickets.remove(encontrado)
            guardar_tickets(tickets)
            print("Ticket eliminado")
    elif opcion != "6":
        print("Opción no válida")
