"""Añade mensajes de inicio y fin sin cambiar la función original."""

def mensaje(funcion):
    def nueva_funcion(*args, **kwargs):
        print("Inicio")
        resultado = funcion(*args, **kwargs)
        print("Fin")
        return resultado
    return nueva_funcion


@mensaje
def mostrar_saludo(nombre):
    print("Bienvenido al sistema,", nombre)


mostrar_saludo("Ana")
