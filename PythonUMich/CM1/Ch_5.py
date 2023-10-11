# Ejercicio 1
sumtot = 0
countot = 0
print('Sum, count and average calculator!')
while True:
    numinp = input('Enter a number: ')
    if numinp == 'done':
        break
    try:
        numinp = float(numinp)
    except:
        print('Invalid data.')
        continue
    sumtot = sumtot + numinp
    countot += 1
print('Sum:', sumtot, 'Count:', countot, 'Average:', sumtot / countot)

# Ejercicio 2
maxyet = None
minyet = None
print('Max and min calculator!')
while True:
    secnuminp = input('Enter a number: ')
    if secnuminp == 'done':
        break
    try:
        secnuminp = float(secnuminp)
    except:
        print('Invalid data')
        continue
    if maxyet is None and minyet is None:
        maxyet = secnuminp
        minyet = secnuminp
    elif secnuminp > maxyet:
        maxyet = secnuminp
    elif secnuminp < minyet:
        minyet = secnuminp
print('Max:', maxyet, "Min:", minyet)
