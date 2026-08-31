class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def describir(self):
        return "Usuario: " + self.nombre


class Cliente(Usuario):
    def describir(self):
        return "Cliente: " + self.nombre


class Tecnico(Usuario):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre)
        self.especialidad = especialidad

    def describir(self):
        return "Técnico: " + self.nombre + " - " + self.especialidad


usuarios = [
    Cliente("Ana"),
    Tecnico("Luis", "Redes"),
    Tecnico("Marta", "Soporte")
]

for usuario in usuarios:
    print(usuario.describir())
