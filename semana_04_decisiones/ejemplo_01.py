"""Clasifica una edad en tres rangos usando decisiones."""

edad = int(input("Edad: "))

if edad <= 0:
    print("La edad no es válida")
elif edad >= 65:
    print("Persona adulta mayor")
elif edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
