"""Calcula el promedio y muestra cuánto falta para alcanzar 71."""

nota_1 = float(input("Primera nota: "))
nota_2 = float(input("Segunda nota: "))
nota_3 = float(input("Tercera nota: "))
suma = nota_1 + nota_2 + nota_3
promedio = suma / 3
faltante = max(0, 71 - promedio)

print("Promedio:", round(promedio, 2))
print("¿El promedio es al menos 71?", promedio >= 71)
print("Puntos que faltan para 71:", round(faltante, 2))
