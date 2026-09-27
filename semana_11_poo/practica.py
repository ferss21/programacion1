"""Practica una clase Ticket con validación y varios objetos."""


class Ticket:
    """Representa una solicitud que puede avanzar por varios estados."""

    ESTADOS = ("Abierto", "En proceso", "Cerrado")
    PRIORIDADES = ("Baja", "Media", "Alta")

    def __init__(self, numero, titulo, descripcion, prioridad):
        if prioridad.title() not in self.PRIORIDADES:
            raise ValueError("Prioridad no válida")
        self.numero = numero
        self.titulo = titulo.strip()
        self.descripcion = descripcion.strip()
        self.prioridad = prioridad.title()
        self.estado = "Abierto"

    def actualizar_estado(self, estado):
        """Cambia el estado solo si pertenece al catálogo permitido."""
        estados = {valor.casefold(): valor for valor in self.ESTADOS}
        estado_normalizado = estados.get(estado.strip().casefold())
        if estado_normalizado is None:
            raise ValueError("Estado no válido")
        self.estado = estado_normalizado

    def esta_pendiente(self):
        return self.estado != "Cerrado"

    def resumen(self):
        return f"#{self.numero} {self.titulo} | {self.prioridad} | {self.estado}"

    def mostrar(self):
        print("\n", self.resumen())
        print("Descripción:", self.descripcion)


tickets = [
    Ticket(1, "Problema de acceso", "No inicia sesión", "Alta"),
    Ticket(2, "Instalar programa", "Instalar editor", "Media"),
    Ticket(3, "Actualizar equipo", "Revisar memoria", "Baja"),
]

tickets[0].actualizar_estado("En proceso")
for ticket in tickets:
    ticket.mostrar()

pendientes = [ticket for ticket in tickets if ticket.esta_pendiente()]
print("\nTickets pendientes:", len(pendientes))
