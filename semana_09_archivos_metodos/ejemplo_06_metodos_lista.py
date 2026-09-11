notas = [80, 95, 80, 71]
notas.append(88)
notas.insert(1, 90)
notas.remove(71)

print("Posición de 95:", notas.index(95))
print("Cantidad de 80:", notas.count(80))
print("Nota retirada:", notas.pop())

notas.sort()
print(notas)
notas.reverse()
print(notas)
