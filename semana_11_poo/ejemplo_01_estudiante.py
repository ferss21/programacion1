"""Representa estudiantes mediante objetos con comportamiento propio."""

class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def mostrar(self):
        print(self.nombre, "-", self.carrera)

    def cambiar_carrera(self, carrera):
        self.carrera = carrera.strip().title()


estudiante_1 = Estudiante("Ana", "Sistemas")
estudiante_1.mostrar()
estudiante_1.cambiar_carrera("administración")
estudiante_1.mostrar()
