nota = float(input("Nota: "))

if nota < 0 or nota > 100:
    print("La nota no es válida")
elif nota >= 71:
    print("Aprobado")
else:
    print("Reprobado")
