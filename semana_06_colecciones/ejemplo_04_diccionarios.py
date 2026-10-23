"""Actualiza y recorre los datos de un estudiante."""

estudiantes = [{
    "nombre": "Ana1",
    "carrera": "Sistemas1",
    "nota": 881
},{
    "nombre": "Ana2",
    "carrera": "Sistemas2",
    "nota": 882
},{
    "nombre": "Ana3",
    "carrera": "Sistemas3",
    "nota": 883
}]
estudiantes.insert(len(estudiantes), {
    "nombre": "Ana4",
    "carrera": "Sistemas4",
    "nota": 884
});
print(len(estudiantes))
for valor in estudiantes:
    print(valor["nombre"], valor["carrera"], valor["nota"])
