"""Administra un inventario en memoria antes de estudiar persistencia."""

inventario = []
opcion = ""

while opcion != "6":
    print("\n1. Agregar  2. Buscar  3. Modificar")
    print("4. Eliminar  5. Mostrar  6. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        codigo = input("Código: ").strip().upper()
        nombre = input("Nombre: ").strip()
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        inventario.append({
            "codigo": codigo,
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
        })
    elif opcion in ("2", "3", "4"):
        codigo = input("Código: ").strip().upper()
        encontrado = None
        for producto in inventario:
            if producto.get("codigo") == codigo:
                encontrado = producto
                break
        if encontrado is None:
            print("Producto no encontrado")
        elif opcion == "2":
            print(encontrado)
        elif opcion == "3":
            encontrado.update({
                "precio": float(input("Nuevo precio: ")),
                "cantidad": int(input("Nueva cantidad: ")),
            })
        else:
            inventario.remove(encontrado)
    elif opcion == "5":
        for producto in inventario:
            total = producto["precio"] * producto["cantidad"]
            print(producto, "- valor:", round(total, 2))
    elif opcion != "6":
        print("Opción no válida")
