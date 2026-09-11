monto = float(input("Monto de compra: "))

if monto >= 100:
    print("Recibe descuento")
elif monto >= 50:
    print("Recibe un descuento menor")
else:
    print("No recibe descuento")
