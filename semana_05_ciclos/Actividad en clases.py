#Construya un programa que reciba varias notas mediante un `while` controlado
#  por cantidad. Calcule promedio, cantidad de aprobados, cantidad de 
# reprobados, nota mayor y nota menor. Ignore notas inválidas usando 
# `continue` y permita finalizar con una opción de salida.
cantidad = int(input("Ingrese la cantidad de notas a procesar: "))
promedio = 0
total = 0
mayor  = 0
menor  = 0
aprobados = 0
reprobados = 0
inicio = 0
while inicio < cantidad:
    nota = float(input("Ingrese una nota (0-100): "))
    if nota < 0 or nota > 100:
        print("Nota inválida, intente nuevamente.")
        continue
    total += nota
    if inicio == 0:
        mayor = nota
        menor = nota
    else:
        if nota > mayor:
            mayor = nota
        if nota < menor:
            menor = nota
    if nota >= 81:
        aprobados += 1
    else:
        reprobados += 1
    promedio += nota
    inicio += 1
promedio = promedio / cantidad   
print (aprobados, reprobados, mayor, menor, promedio)