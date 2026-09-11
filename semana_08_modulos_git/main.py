import calculos
from mensajes import mostrar_titulo
from mensajes import despedir as finalizar


mostrar_titulo("Módulos propios")
print("Suma:", calculos.sumar(10, 7))
print("Promedio:", calculos.calcular_promedio([80, 95, 72]))
print("Descuento:", calculos.calcular_descuento(150, 10))
finalizar()
