from pathlib import Path


ruta = Path(__file__).with_name("nombres.txt")


def guardar_nombre(nombre):
    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(nombre + "\n")


def mostrar_nombres():
    ruta.touch(exist_ok=True)
    with open(ruta, "r", encoding="utf-8") as archivo:
        print(archivo.read())


guardar_nombre("Ana")
mostrar_nombres()
