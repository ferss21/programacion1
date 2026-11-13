"""ACTIVIDAD 1 RESUELTA — Mis calificaciones.

Cree un programa que muestre el promedio de unas notas e indique si alcanza
71 puntos. Puede elegir las notas y la forma de presentar el resultado.

Análisis: las entradas son un nombre y una lista de notas; el proceso consiste
en sumar, dividir y comparar; la salida es un resumen del estudiante.
Pseudocódigo: pedir nombre, recorrer las notas, calcular promedio y mostrar
si aprobó. Esta solución usa notas de ejemplo para facilitar su revisión.

Temas: entrada y salida, variables, números, strings, operadores, decisiones,
ciclos, listas, tuplas, diccionarios, métodos y funciones con parámetros y return.
"""


def calcular_promedio(notas):
    total = 0
    for nota in notas:
        total += nota
    return total / len(notas)


def main():
    nombre = input("¿Cómo te llamas? ").strip().title()
    notas = [75, 80, 85]
    limites = (0, 100)

    # Comprobamos que haya notas y que estén dentro de la escala.
    if len(notas) == 0:
        print("Agrega al menos una nota.")
        return
    for nota in notas:
        if nota < limites[0] or nota > limites[1]:
            print("Las notas deben estar entre 0 y 100.")
            return

    promedio = calcular_promedio(notas)
    if promedio >= 71:
        estado = "Aprobado"
    else:
        estado = "Reprobado"

    estudiante = {"nombre": nombre, "promedio": promedio, "estado": estado}
    for dato, valor in estudiante.items():
        print(dato, ":", valor)


if __name__ == "__main__":
    main()

# Con las notas de ejemplo, el promedio es 80.0 y el estado es Aprobado.
# Cambia las notas para probar otro resultado.
