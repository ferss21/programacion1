def pedir_producto():
    nombre = input("Producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    return nombre, precio, cantidad


def calcular_total(precio, cantidad):
    subtotal = precio * cantidad
    impuesto = subtotal * 0.07
    return subtotal, impuesto, subtotal + impuesto


def mostrar_factura(nombre, subtotal, impuesto, total):
    print("\nProducto:", nombre)
    print("Subtotal:", round(subtotal, 2))
    print("ITBMS:", round(impuesto, 2))
    print("Total:", round(total, 2))


producto, precio, cantidad = pedir_producto()
subtotal, impuesto, total = calcular_total(precio, cantidad)
mostrar_factura(producto, subtotal, impuesto, total)
