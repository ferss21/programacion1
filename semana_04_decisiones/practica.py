nombre = input("Nombre del estudiante: ")
nota = float(input("Nota: "))
asistencia = float(input("Porcentaje de asistencia: "))

if nota < 0 or nota > 100 or asistencia < 0 or asistencia > 100:
    print("Los datos no son válidos")
elif nota >= 71 and asistencia >= 75:
    print(nombre, "aprobó")
elif nota >= 68 and asistencia >= 75:
    print(nombre, "necesita revisión")
else:
    print(nombre, "reprobó")
