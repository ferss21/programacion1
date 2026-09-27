"""Construye un recibo sencillo con descuento e impuesto."""

producto = input("Producto: ").strip()
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))
porcentaje_descuento = float(input("Descuento (%): "))

subtotal = precio * cantidad
descuento = subtotal * porcentaje_descuento / 100
base_impuesto = subtotal - descuento
itbms = base_impuesto * 0.07
total = base_impuesto + itbms

print("\n===== RECIBO =====")
print("Producto:", producto)
print("Cantidad:", cantidad)
print("Subtotal:", round(subtotal, 2))
print("Descuento:", round(descuento, 2))
print("ITBMS:", round(itbms, 2))
print("Total:", round(total, 2))
