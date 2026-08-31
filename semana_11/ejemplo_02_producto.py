class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.precio * self.cantidad

    def mostrar(self):
        print(self.nombre, "- Subtotal:", self.calcular_subtotal())


producto = Producto("Cuaderno", 3.50, 4)
producto.mostrar()
