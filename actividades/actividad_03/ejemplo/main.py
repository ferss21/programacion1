def calcular_promedio(notas):
    return sum(notas) / len(notas)


def aprobo(promedio):
    return promedio >= 71


notas = [80, 75, 90]
promedio = calcular_promedio(notas)
print("Promedio:", promedio)
print("Aprobó:", aprobo(promedio))
