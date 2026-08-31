from pathlib import Path


ruta = Path(__file__).with_name("mensaje.bin")
mensaje = "Ejemplo de archivo binario"

with open(ruta, "wb") as archivo:
    archivo.write(mensaje.encode("utf-8"))

with open(ruta, "rb") as archivo:
    datos = archivo.read()

print(datos.decode("utf-8"))
