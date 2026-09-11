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
        print("\nTicket", self.numero)
        print("Título:", self.titulo)
        print("Descripción:", self.descripcion)
        print("Prioridad:", self.prioridad)
        print("Estado:", self.estado)


ticket = Ticket(
    1,
    input("Título: "),
    input("Descripción: "),
    input("Prioridad: ")
)
ticket.mostrar()
ticket.actualizar_estado("En proceso")
ticket.mostrar()
