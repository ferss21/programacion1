"""Aplica polimorfismo a resúmenes de tickets."""

class Ticket:
    def __init__(self, titulo):
        self.titulo = titulo

    def mostrar(self):
        print("Ticket:", self.titulo)

    def tiempo_estimado(self):
        return 3


class TicketUrgente(Ticket):
    def __init__(self, titulo, motivo):
        super().__init__(titulo)
        self.motivo = motivo

    def mostrar(self):
        print("Ticket urgente:", self.titulo, "-", self.motivo)

    def tiempo_estimado(self):
        return 1


tickets = [Ticket("Cambiar contraseña"), TicketUrgente("Servidor caído", "Sin servicio")]
for ticket in tickets:
    ticket.mostrar()
    print("Horas estimadas:", ticket.tiempo_estimado())
