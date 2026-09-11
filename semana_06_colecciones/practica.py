estudiantes = []
cantidad = int(input("Cantidad de estudiantes: "))

for posicion in range(cantidad):
    print("\nEstudiante", posicion + 1)
    nombre = input("Nombre: ")
    nota = float(input("Nota: "))
    estudiantes.append({"nombre": nombre, "nota": nota})

print("\nRegistro de estudiantes")
for estudiante in estudiantes:
    if estudiante["nota"] >= 71:
        resultado = "aprobó"
    else:
        resultado = "reprobó"
    print(estudiante["nombre"], "-", estudiante["nota"], "-", resultado)
