from pathlib import Path


ruta = Path(__file__).with_name("tickets.txt")
opcion = ""

while opcion != "3":
    print("\n1. Registrar ticket")
    print("2. Consultar tickets")
    print("3. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        titulo = input("Título: ")
        prioridad = input("Prioridad: ")
        with open(ruta, "a", encoding="utf-8") as archivo:
            archivo.write(titulo + " | " + prioridad + "\n")
        print("Ticket guardado")
    elif opcion == "2":
        ruta.touch(exist_ok=True)
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
        print(contenido if contenido else "No hay tickets")
    elif opcion != "3":
        print("Opción no válida")
