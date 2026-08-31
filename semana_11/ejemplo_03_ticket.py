class Ticket:
    def __init__(self, numero, titulo, prioridad):
        self.numero = numero
        self.titulo = titulo
        self.prioridad = prioridad
        self.estado = "Abierto"

    def cerrar(self):
        self.estado = "Cerrado"

    def mostrar(self):
        print(self.numero, self.titulo, self.prioridad, self.estado)


ticket = Ticket(1, "Problema de acceso", "Alta")
ticket.mostrar()
ticket.cerrar()
ticket.mostrar()
