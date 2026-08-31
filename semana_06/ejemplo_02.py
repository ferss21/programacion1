def calcular_promedio(notas):
    total = 0
    for nota in notas:
        total += nota
    return total / len(notas)


def validar_nota(nota):
    return nota >= 0 and nota <= 100


notas = [85, 90, 76]
print("Promedio:", calcular_promedio(notas))
print("¿Nota válida?", validar_nota(105))
