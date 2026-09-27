"""Muestra una cuenta regresiva para introducir el caso base."""

def cuenta_regresiva(numero):
    if numero == 0:
        print("Inicio")
        return
    print(numero)
    cuenta_regresiva(numero - 1)


cuenta_regresiva(5)
