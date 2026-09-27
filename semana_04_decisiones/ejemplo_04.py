"""Calcula descuento y clasificación de una compra."""

monto = float(input("Monto de la compra: "))

if monto < 0:
    print("El monto no es válido")
else:
    if monto >= 200:
        descuento = monto * 0.15
        categoria = "cliente preferente"
    elif monto >= 100:
        descuento = monto * 0.10
        categoria = "cliente regular"
    else:
        descuento = 0
        categoria = "compra básica"

    print("Descuento:", round(descuento, 2))
    print("Total:", round(monto - descuento, 2))
    print("Categoría:", categoria)
