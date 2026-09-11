opcion = ""

while opcion != "4":
    print("\n1. Saludar")
    print("2. Mostrar números")
    print("3. Tabla de multiplicar")
    print("4. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        print("Hola", nombre)
    elif opcion == "2":
        for numero in range(1, 11):
            print(numero)
    elif opcion == "3":
        tabla = int(input("Tabla: "))
        for numero in range(1, 11):
            print(tabla, "x", numero, "=", tabla * numero)
    elif opcion == "4":
        print("Hasta luego")
    else:
        print("Opción no válida")
