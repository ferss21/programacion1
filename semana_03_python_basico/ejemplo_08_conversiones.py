"""Realiza dos conversiones independientes con datos ingresados."""

celsius = float(input("Temperatura en Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print("Temperatura en Fahrenheit:", round(fahrenheit, 2))

horas = float(input("Horas trabajadas: "))
pago_por_hora = float(input("Pago por hora: "))
salario = horas * pago_por_hora
print("Horas trabajadas:", horas)
print("Pago por hora:", round(pago_por_hora, 2))
print("Salario básico:", round(salario, 2))
