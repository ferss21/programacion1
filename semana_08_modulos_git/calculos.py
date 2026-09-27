"""Funciones de cálculo sin interacción con la consola."""

def sumar(a, b):
    return a + b


def calcular_promedio(notas):
    return sum(notas) / len(notas)


def calcular_descuento(monto, porcentaje):
    return monto * porcentaje / 100


def calcular_total(monto, porcentaje_descuento, porcentaje_impuesto):
    descuento = calcular_descuento(monto, porcentaje_descuento)
    base = monto - descuento
    impuesto = base * porcentaje_impuesto / 100
    return descuento, impuesto, base + impuesto
