"""Registra estudiantes y calcula un resumen del grupo."""

estudiantes = []
cantidad = int(input("Cantidad de estudiantes: "))

for posicion in range(cantidad):
    print("\nEstudiante", posicion + 1)
    nombre = input("Nombre: ")
    nota = float(input("Nota: "))
    estudiantes.append({"nombre": nombre, "nota": nota})

print("\nRegistro de estudiantes")
aprobados = 0
total_notas = 0

for estudiante in estudiantes:
    if estudiante["nota"] >= 71:
        resultado = "aprobó"
        aprobados += 1
    else:
        resultado = "reprobó"
    total_notas += estudiante["nota"]
    print(estudiante["nombre"], "-", estudiante["nota"], "-", resultado)

if estudiantes:
    print("\nPromedio del grupo:", round(total_notas / len(estudiantes), 2))
    print("Aprobados:", aprobados)
    busqueda = input("Buscar estudiante: ").strip().lower()
    encontrados = [e for e in estudiantes if busqueda in e["nombre"].lower()]
    print("Coincidencias:", encontrados if encontrados else "Ninguna")
