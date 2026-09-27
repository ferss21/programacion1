"""Calcula el recibo de dos productos usando operaciones básicas."""

nombre_1 = input("Nombre del primer producto: ")
precio_1 = float(input("Precio del primer producto: "))
cantidad_1 = int(input("Cantidad del primer producto: "))
nombre_2 = input("Nombre del segundo producto: ")
precio_2 = float(input("Precio del segundo producto: "))
cantidad_2 = int(input("Cantidad del segundo producto: "))

subtotal_1 = precio_1 * cantidad_1
subtotal_2 = precio_2 * cantidad_2
subtotal = subtotal_1 + subtotal_2
impuesto = subtotal * 0.07
total = subtotal + impuesto

print("\n===== RECIBO =====")
print(nombre_1, "x", cantidad_1, "=", round(subtotal_1, 2))
print(nombre_2, "x", cantidad_2, "=", round(subtotal_2, 2))
print("Subtotal:", round(subtotal, 2))
print("ITBMS:", round(impuesto, 2))
print("Total:", round(total, 2))
