"""Actualiza y recorre los datos de un estudiante."""

estudiante = {
    "nombre": "Ana",
    "carrera": "Sistemas",
    "nota": 88
}

print(estudiante["nombre"])
estudiante["nota"] = 91
estudiante["correo"] = "ana@ejemplo.com"

for clave, valor in estudiante.items():
    print(clave, ":", valor)

del estudiante["correo"]
