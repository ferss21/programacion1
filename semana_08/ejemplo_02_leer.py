from pathlib import Path


ruta = Path(__file__).with_name("estudiantes.txt")
ruta.touch(exist_ok=True)

with open(ruta, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

if contenido:
    print(contenido)
else:
    print("El archivo está vacío")
