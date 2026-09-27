"""Determina el resultado de un estudiante con varias condiciones."""

nombre = input("Nombre del estudiante: ").strip()
nota = float(input("Nota: "))
asistencia = float(input("Porcentaje de asistencia: "))
proyecto = input("¿Entregó el proyecto? (s/n): ").strip().lower()

if (nota < 0 or nota > 100 or asistencia < 0 or asistencia > 100
        or proyecto not in ("s", "n")):
    print("Los datos no son válidos")
elif nota >= 71 and asistencia >= 75 and proyecto == "s":
    print(nombre, "aprobó")
elif nota >= 68 and asistencia >= 75 and proyecto == "s":
    print(nombre, "necesita revisión")
else:
    print(nombre, "reprobó")
