# EjercicioF 1
inputtxt = input("Nombre de archivo (con extensión): ")
if inputtxt == "fuck u":
    print("no u")
    exit()
try:
    fileh = open(inputtxt, "r")
except:
    print("Haga eso bien")
    exit()

palabras = []
for line in fileh:
    line.rstrip()
    linea = line.split()
    for w in linea:
        if w not in palabras:
            palabras.append(w)
        else:
            continue

palabras.sort()
print(palabras)

# EjercicioF 2
pl2 = []
for line in fileh:
    if not line.startswith("From") or line.startswith("From:"):
        continue
    line.rstrip()
    linea = line.split()
    pl2.append(linea[1])

print(pl2)
print("Cantidad:", len(pl2))

# EjercicioF 3
nlst = []
entrada = None

while 1:
    entrada = input("Indique un número (exit pa salir): ")
    if entrada == "exit":
        break
    try:
        nlst.append(float(entrada))
    except:
        print("jodete")
        continue

try:
    print("Max:", max(nlst))
    print("Min:", min(nlst))
except:
    print("Haga eso bien")