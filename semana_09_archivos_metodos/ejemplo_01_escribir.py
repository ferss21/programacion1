"""Escribe varias líneas usando un administrador de contexto."""

from pathlib import Path


ruta = Path(__file__).with_name("nombres.txt")

with open(ruta, "w", encoding="utf-8") as archivo:
    archivo.write("Ana\n")
    archivo.write("Luis\n")

print("Nombres guardados")
