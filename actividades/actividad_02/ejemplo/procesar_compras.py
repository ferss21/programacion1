total = 0
cantidad = int(input("¿Cuántas compras desea procesar? "))

for posicion in range(cantidad):
    monto = float(input("Monto de la compra: "))

    if monto >= 100:
        descuento = monto * 0.10
    else:
        descuento = 0

    total += monto - descuento
    print("Total de esta compra:", round(monto - descuento, 2))

print("Total acumulado:", round(total, 2))
