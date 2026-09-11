precio_1 = float(input("Precio del primer producto: "))
precio_2 = float(input("Precio del segundo producto: "))
subtotal = precio_1 + precio_2
impuesto = subtotal * 0.07

print("Subtotal:", subtotal)
print("ITBMS:", impuesto)
print("Total:", subtotal + impuesto)
