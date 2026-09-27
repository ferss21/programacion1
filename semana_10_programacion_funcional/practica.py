"""Combina un generador de notas con un decorador de reportes."""

def anunciar(funcion):
    def ejecutar(*args, **kwargs):
        print("--- Iniciando reporte ---")
        resultado = funcion(*args, **kwargs)
        print("--- Reporte terminado ---")
        return resultado
    return ejecutar


def notas_aprobadas(notas, minimo=71):
    for nota in notas:
        if nota >= minimo:
            yield nota


@anunciar
def mostrar_reporte(notas):
    for nota in notas_aprobadas(notas, minimo=71):
        print(nota)


mostrar_reporte([65, 82, 90, 70, 75])
