# Ejercicio 1
banana = "banana"
lenght = len(banana)-1

while lenght > -1:
    print(banana[lenght])
    lenght -= 1

# Ejercicio 2
def count(wordo, lettero):
    print("Vamo a contar cuantas hay de una letra")
    counto = 0
    for find in wordo:
        if find == lettero:
            counto += 1
    print(counto)
    return counto

print("Total de veces:", count(input("Palabra: "), input("Letra: ")))

# Ejercicio 3
waurdo = str(input("Palabra de nuevo!: "))
letturo = str(input("Letra again: "))

print("Le gran totale:", waurdo.count(letturo))

# Ejercicio 4
sutringu = 'X-DSPAM-Confidence:0.8475'

sutartu = sutringu.find(":")
finalst = float(sutringu[sutartu+1:])

print(finalst, type(finalst))
