"""Explora métodos de texto útiles para normalizar entradas."""

mensaje = "  Programación en Python  "

print("Texto original:", mensaje)
print("Cantidad de caracteres:", len(mensaje))
print("Primer carácter:", mensaje[0])
print("Mayúsculas:", mensaje.upper())
print("Minúsculas:", mensaje.lower())
print("Sin espacios:", mensaje.strip())
print("Posición de Python:", mensaje.find("Python"))
print("Reemplazo:", mensaje.replace("Python", "clase"))
print("Palabras:", mensaje.strip().split())
