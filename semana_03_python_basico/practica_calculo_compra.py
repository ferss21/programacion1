producto = input("Producto: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

subtotal = precio * cantidad
itbms = subtotal * 0.07
total = subtotal + itbms

print("\nProducto:", producto)
print("Subtotal:", round(subtotal, 2))
print("ITBMS:", round(itbms, 2))
print("Total:", round(total, 2))
