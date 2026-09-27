"""Acumula números positivos hasta recibir cero."""

total = 0
cantidad = 0

while True:
    numero = int(input("Escriba un número positivo (0 para terminar): "))
    if numero == 0:
        break
    if numero < 0:
        print("Se omiten los números negativos")
        continue
    print("Ingresó:", numero)
    total += numero
    cantidad += 1

if cantidad:
    print("Cantidad:", cantidad)
    print("Promedio:", round(total / cantidad, 2))
else:
    print("No se ingresaron positivos")
