class Usuario:
    def mostrar_tipo(self):
        print("Usuario")


class Cliente(Usuario):
    def mostrar_tipo(self):
        print("Cliente")


class Tecnico(Usuario):
    def mostrar_tipo(self):
        print("Técnico")


usuarios = [Usuario(), Cliente(), Tecnico()]
for usuario in usuarios:
    usuario.mostrar_tipo()
