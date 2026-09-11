from calculos import calcular_descuento


monto = float(input("Monto de la compra: "))
porcentaje = float(input("Porcentaje de descuento: "))
descuento = calcular_descuento(monto, porcentaje)

print("Descuento:", round(descuento, 2))
print("Total:", round(monto - descuento, 2))
