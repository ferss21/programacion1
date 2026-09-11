cantidad = int(input("¿Cuántas notas ingresará? "))
total = 0
aprobados = 0

for posicion in range(cantidad):
    nota = float(input("Nota: "))
    total += nota
    if nota >= 71:
        aprobados += 1

if cantidad > 0:
    print("Promedio:", total / cantidad)
print("Aprobados:", aprobados)
