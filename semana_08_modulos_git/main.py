"""Punto de entrada que coordina módulos propios."""

import calculos
from mensajes import mostrar_titulo
from mensajes import mostrar_resumen
from mensajes import despedir as finalizar


mostrar_titulo("Módulos propios")
print("Suma:", calculos.sumar(10, 7))
print("Promedio:", calculos.calcular_promedio([80, 95, 72]))
print("Descuento:", calculos.calcular_descuento(150, 10))
descuento, impuesto, total = calculos.calcular_total(150, 10, 7)
mostrar_resumen(150, descuento, impuesto, total)
finalizar()
