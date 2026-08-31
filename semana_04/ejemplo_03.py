while True:
    numero = int(input("Escriba un número positivo (0 para terminar): "))
    if numero == 0:
        break
    if numero < 0:
        print("Se omiten los números negativos")
        continue
    print("Ingresó:", numero)
