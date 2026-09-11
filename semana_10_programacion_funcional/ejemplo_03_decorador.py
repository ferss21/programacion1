def mensaje(funcion):
    def nueva_funcion():
        print("Inicio")
        funcion()
        print("Fin")
    return nueva_funcion


@mensaje
def mostrar_saludo():
    print("Bienvenido al sistema")


mostrar_saludo()
