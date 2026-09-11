from pathlib import Path


ruta = Path(__file__).with_name("notas.txt")
nombre = input("Nombre: ")
nota = input("Nota: ")

with open(ruta, "a", encoding="utf-8") as archivo:
    archivo.write(nombre + "," + nota + "\n")

print("Nota guardada")
