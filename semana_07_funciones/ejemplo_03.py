"""Busca registros sin exponer la lógica de búsqueda al programa principal."""

def buscar_estudiante(estudiantes, nombre):
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            return estudiante
    return None


estudiantes = [
    {"nombre": "Ana", "nota": 90},
    {"nombre": "Luis", "nota": 75}
]

encontrado = buscar_estudiante(estudiantes, input("Nombre: "))
if encontrado:
    print(encontrado)
    print("Resultado:", "aprobado" if encontrado["nota"] >= 71 else "reprobado")
else:
    print("Estudiante no encontrado")
