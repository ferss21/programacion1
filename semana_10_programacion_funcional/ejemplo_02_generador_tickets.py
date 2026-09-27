"""Filtra tickets abiertos de manera diferida."""

def tickets_abiertos(tickets):
    for ticket in tickets:
        if ticket["estado"] == "Abierto":
            yield ticket


datos = [
    {"titulo": "Sin acceso", "estado": "Abierto"},
    {"titulo": "Instalar programa", "estado": "Cerrado"},
    {"titulo": "Error de impresora", "estado": "Abierto"}
]

for ticket in tickets_abiertos(datos):
    print(ticket["titulo"], "-", ticket["estado"])
