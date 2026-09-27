"""Calcula el valor de productos mediante un método de instancia."""

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.precio * self.cantidad

    def aplicar_descuento(self, porcentaje):
        return self.calcular_subtotal() * (1 - porcentaje / 100)

    def mostrar(self):
        print(self.nombre, "- Subtotal:", self.calcular_subtotal())


producto = Producto("Cuaderno", 3.50, 4)
producto.mostrar()
print("Con descuento:", round(producto.aplicar_descuento(10), 2))
