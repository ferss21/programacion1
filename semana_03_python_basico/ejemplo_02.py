"""Lee texto y convierte una entrada a entero."""

# input permite recibir información del teclado
nombre = input("¿Cómo te llamas? ")
print("Hola", nombre)

edad = input("¿Cuántos años tienes? ")
edad = int(edad) - 5
print("Tu edad es", edad)
print(nombre, "tiene", edad, "años")
