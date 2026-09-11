class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def mostrar(self):
        print(self.nombre, "-", self.carrera)


estudiante_1 = Estudiante("Ana", "Sistemas")
estudiante_1.mostrar()
estudiante_1.carrera = "Administración"
estudiante_1.mostrar()
