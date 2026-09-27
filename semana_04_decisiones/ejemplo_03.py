"""Valida una nota y determina su resultado académico."""

nota = float(input("Nota: "))
asistencia = float(input("Asistencia (%): "))

if nota < 0 or nota > 100 or asistencia < 0 or asistencia > 100:
    print("La nota no es válida")
elif nota >= 71 and asistencia >= 75:
    print("Aprobado")
elif nota >= 68 and asistencia >= 75:
    print("Aprobado con observación")
else:
    print("Reprobado")
