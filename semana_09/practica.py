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
        inventario.append({"codigo": codigo, "nombre": nombre, "precio": precio})
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
            encontrado.update({"precio": float(input("Nuevo precio: "))})
        else:
            inventario.remove(encontrado)
    elif opcion == "5":
        for producto in inventario:
            print(producto)
    elif opcion != "6":
        print("Opción no válida")
