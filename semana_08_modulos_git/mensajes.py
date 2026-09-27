"""Mensajes reutilizables para la interfaz de consola."""

def mostrar_titulo(texto):
    print("\n=====", texto.upper(), "=====")


def despedir():
    print("Programa finalizado")


def mostrar_resumen(monto, descuento, impuesto, total):
    print("\n===== RESUMEN =====")
    print("Monto:", round(monto, 2))
    print("Descuento:", round(descuento, 2))
    print("Impuesto:", round(impuesto, 2))
    print("Total:", round(total, 2))
