"""Administra una lista de productos y genera un pequeño reporte."""

productos = ["cuaderno", "lápiz", "regla"]
productos.append("borrador")
productos[1] = "bolígrafo"

for producto in productos:
    print(producto)

busqueda = input("Producto que desea buscar: ").lower()
if busqueda in productos:
    print("Producto encontrado")
else:
    print("Producto no encontrado")

productos.remove("regla")
print("Productos restantes:", len(productos))
print(productos)
