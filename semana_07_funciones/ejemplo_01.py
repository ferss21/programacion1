"""Ejemplo de funciones con efectos y con valores de retorno."""

def saludar(nombre):
    print("Hola", nombre)


def sumar(a, b):
    return a + b


def multiplicar(a, b):
    return a * b


saludar("Laura")
resultado = sumar(8, 5)
print("Resultado:", resultado)
print("Producto:", multiplicar(8, 5))
