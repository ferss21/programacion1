"""Determina el signo y la paridad de un número entero."""

numero = int(input("Número entero: "))

if numero > 0:
    signo = "Positivo"
elif numero < 0:
    signo = "Negativo"
else:
    signo = "Cero"

if numero == 0:
    paridad = "no aplica"
elif numero % 2 == 0:
    paridad = "par"
else:
    paridad = "impar"

print(signo)
print("Paridad:", paridad)
