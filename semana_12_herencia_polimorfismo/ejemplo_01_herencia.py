class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_tipo(self):
        print(self.nombre, "es un usuario")


class Cliente(Usuario):
    def __init__(self, nombre, empresa):
        super().__init__(nombre)
        self.empresa = empresa

    def mostrar_tipo(self):
        print(self.nombre, "es cliente de", self.empresa)


cliente = Cliente("María", "Empresa Ejemplo")
cliente.mostrar_tipo()
