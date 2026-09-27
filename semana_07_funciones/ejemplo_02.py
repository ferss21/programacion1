"""Calcula resultados reutilizables a partir de una colección."""

def calcular_promedio(notas):
    total = 0
    for nota in notas:
        total += nota
    return total / len(notas)


def validar_nota(nota):
    return nota >= 0 and nota <= 100


def contar_aprobadas(notas):
    return sum(1 for nota in notas if nota >= 71)


notas = [85, 90, 76]
print("Promedio:", calcular_promedio(notas))
print("¿Nota válida?", validar_nota(105))
print("Aprobadas:", contar_aprobadas(notas))
