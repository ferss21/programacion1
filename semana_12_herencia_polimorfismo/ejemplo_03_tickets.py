class Ticket:
    def __init__(self, titulo):
        self.titulo = titulo

    def mostrar(self):
        print("Ticket:", self.titulo)


class TicketUrgente(Ticket):
    def __init__(self, titulo, motivo):
        super().__init__(titulo)
        self.motivo = motivo

    def mostrar(self):
        print("Ticket urgente:", self.titulo, "-", self.motivo)


tickets = [Ticket("Cambiar contraseña"), TicketUrgente("Servidor caído", "Sin servicio")]
for ticket in tickets:
    ticket.mostrar()
