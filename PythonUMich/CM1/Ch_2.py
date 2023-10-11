# Ejercicio 1
nombre = input('Dime tu namae pls: ')
print('Hola,',nombre + '!')

# Ejercicio 2
tiempo = input('Horas: ')
salario = input('Salario por Hora: ')
pago = round(float(tiempo) * float(salario), 2)
print('Pago:', pago)

# Ejercicio 3
print('Conversor Celsius a Fahrenheit!')
celsinp = input('Temperatura en Celsius: ')
fahrout = round((float(celsinp) * 9 / 5) + 32, 2)
print('Temperatura en Fahrenheit:', fahrout)
