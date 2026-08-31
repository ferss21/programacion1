producto = {"nombre": "Teclado", "precio": 25.50, "cantidad": 4}

print(producto.get("nombre"))
print(producto.get("marca", "Sin marca"))
print(producto.keys())
print(producto.values())

producto.update({"precio": 24.00, "marca": "Ejemplo"})
for clave, valor in producto.items():
    print(clave, valor)

producto.pop("marca")
