"""Muestra una secuencia y una tabla usando ciclos for."""

for numero in range(1, 11):
    print(numero)

tabla = int(input("¿Qué tabla desea ver? "))
limite = int(input("¿Hasta qué número?: "))
for numero in range(1, limite + 1):
    print(tabla, "x", numero, "=", tabla * numero)
