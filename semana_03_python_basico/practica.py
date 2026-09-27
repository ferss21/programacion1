"""Calcula el precio final de un producto con descuento e impuesto."""

# escribe creen en un sistema que calcule una promocion de 10 % de descuento
producto = float(input("Precio del producto: "))
descuento = producto * 0.1
total = producto - descuento
impuesto = total * 0.07
total = total + impuesto
print("El precio con descuento es:", total)
