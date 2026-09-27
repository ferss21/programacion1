"""Modela un ticket y controla sus cambios de estado."""

class Ticket:
    def __init__(self, numero, titulo, prioridad):
        self.numero = numero
        self.titulo = titulo
        self.prioridad = prioridad
        self.estado = "Abierto"

    def cerrar(self):
        self.estado = "Cerrado"

    def poner_en_proceso(self):
        if self.estado == "Abierto":
            self.estado = "En proceso"
            return True
        return False

    def mostrar(self):
        print(self.numero, self.titulo, self.prioridad, self.estado)


ticket = Ticket(1, "Problema de acceso", "Alta")
ticket.mostrar()
ticket.poner_en_proceso()
ticket.mostrar()
ticket.cerrar()
ticket.mostrar()
