import string

# Abrir archivo
fileh = None
inputtxt = input("Nombre de archivo (con extensión): ")
if inputtxt == "fuk u":
    print("no u")
    exit()
try:
    fileh = open(inputtxt, "r")
except:
    print("Haga eso bien")
    exit()

# Ejercicio 1
remitente = {}
for line in fileh:
    if not line.startswith("From") or line.startswith("From: "):
        continue
    line.rstrip()
    linea = line.split()
    remitente[linea[1]] = remitente.get(linea[1], 0) + 1

lisrem = remitente.items()
temmie = sorted([(k, v) for v, k in lisrem], reverse=True)

for a, b in temmie[:10]:
    print(b, a)

# Ejercicio 2
hora = {}
for line2 in fileh:
    if not line2.startswith("From") or line2.startswith("From: "):
        continue
    line2.rstrip()
    linea2 = line2.split()
    sublinea2 = linea2[5].split(":")
    hora[sublinea2[0]] = hora.get(sublinea2[0], 0) + 1

lishor = hora.items()
toby = sorted([(k, v) for v, k in lishor], reverse=True)

for a, b in toby[:10]:
    print(b, a)

# Ejercicio 3
letemp = []
letras = {}
for line3 in fileh:
    line3.rstrip()
    line3 = line3.translate(line3.maketrans('', '', string.punctuation)) # ????
    line3 = line3.lower()
    linea3 = line3.split()
    for i in linea3:
        letemp.extend(list(i))

for l in letemp:
    letras[l] = letras.get(l, 0) + 1

ledef = letras.items()
nightm = sorted([(k,v) for v, k in ledef], reverse=True)

for c, d in nightm[:10]:
    print(d, c)
