"""Calcula estadísticas de un grupo de notas válidas."""

cantidad = int(input("¿Cuántas notas ingresará? "))
total = 0
aprobados = 0
reprobados = 0
mayor = None
menor = None

for posicion in range(cantidad):
    nota = float(input("Nota: "))
    if nota < 0 or nota > 100:
        print("Nota inválida; no se cuenta")
        continue
    total += nota
    if nota >= 71:
        aprobados += 1
    else:
        reprobados += 1
    if mayor is None or nota > mayor:
        mayor = nota
    if menor is None or nota < menor:
        menor = nota

validas = aprobados + reprobados
if validas > 0:
    print("Promedio:", round(total / validas, 2))
    print("Mayor:", mayor)
    print("Menor:", menor)
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
