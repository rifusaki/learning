# Ejercicio 1
print('¡Calculadora de pago!')
print('Se tomará el salario normal hasta 40 horas trabajadas; más de 40 se pagará a 1.5x.')
tiempo = float(input('Horas: '))
salario = float(input('Salario: '))
if float(tiempo) <= 40:
    pago = round(salario * tiempo, 2)
else:
    pago = round((salario * 40.0) + ((tiempo - 40) * salario * 1.5))
print('Pago total:', pago)

# Ejercicio 2
print('¡Calculadora de pago!')
print('Se tomará el salario normal hasta 40 horas trabajadas; más de 40 se pagará a 1.5x.')
try:
    tiempo = float(input('Horas: '))
    salario = float(input('Salario: '))
except:
    print('Error, por favor introduce únicamente números')
    quit()
if tiempo <= 40:
    pago = round(salario * tiempo, 2)
else:
    pago = round((salario * 40.0) + ((tiempo - 40) * salario * 1.5))
print('Pago total:', pago)

# Ejercicio 3
print('¡Puntaje a nota!')
puntinp = input('Por favor, introduce un puntaje de 0.0 a 1.0: ')
notout = ''
try:
    puntinp = float(puntinp)
except:
    puntinp = -1
if puntinp == -1 or puntinp > 1.0:
    print('Introduce números de 0.0 a 1.0')
else:
    if puntinp >= 0.9:
        notout = 'A'
    elif puntinp >= 0.8:
        notout = 'B'
    elif puntinp >= 0.7:
        notout = 'C'
    elif puntinp >= 0.6:
        notout = 'D'
    elif puntinp < 0.6:
        notout = 'F'
    print('Nota:', notout)
