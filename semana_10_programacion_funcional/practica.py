def anunciar(funcion):
    def ejecutar():
        print("--- Iniciando reporte ---")
        funcion()
        print("--- Reporte terminado ---")
    return ejecutar


def notas_aprobadas(notas):
    for nota in notas:
        if nota >= 71:
            yield nota


@anunciar
def mostrar_reporte():
    notas = [65, 82, 90, 70, 75]
    for nota in notas_aprobadas(notas):
        print(nota)


mostrar_reporte()
