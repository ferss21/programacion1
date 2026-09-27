"""Usa un módulo propio para calcular un recibo."""

from calculos import calcular_total


monto = float(input("Monto de la compra: "))
porcentaje = float(input("Porcentaje de descuento: "))
impuesto = float(input("Porcentaje de impuesto: "))
descuento, impuesto_calculado, total = calcular_total(monto, porcentaje, impuesto)

print("Descuento:", round(descuento, 2))
print("Impuesto:", round(impuesto_calculado, 2))
print("Total:", round(total, 2))
