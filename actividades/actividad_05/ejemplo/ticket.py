class Ticket:
    def __init__(self, numero, titulo, descripcion, prioridad):
        self.numero = numero
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = "Abierto"

    def actualizar_estado(self, estado):
        self.estado = estado

    def mostrar(self):
        print(self.numero, self.titulo, self.prioridad, self.estado)


ticket_1 = Ticket(1, "Problema de acceso", "No inicia sesión", "Alta")
ticket_2 = Ticket(2, "Instalar programa", "Instalar editor", "Media")
tickets = [ticket_1, ticket_2]

for ticket in tickets:
    ticket.mostrar()

ticket_1.actualizar_estado("En proceso")
ticket_1.mostrar()
