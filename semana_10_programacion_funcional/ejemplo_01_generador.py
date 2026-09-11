def numeros(limite):
    for numero in range(1, limite + 1):
        yield numero


for numero in numeros(5):
    print(numero)
