class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def mostrar(self):
        print(self.codigo, self.nombre, self.precio)


producto = Producto("P01", "Cuaderno", 3.50)
producto.cambiar_precio(3.75)
producto.mostrar()
