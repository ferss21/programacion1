productos = [
    {"codigo": "P01", "nombre": "Cuaderno"},
    {"codigo": "P02", "nombre": "Lápiz"}
]

codigo = input("Código que desea buscar: ").upper()
for producto in productos:
    if producto["codigo"] == codigo:
        print(producto["nombre"])
        break
else:
    print("No encontrado")
