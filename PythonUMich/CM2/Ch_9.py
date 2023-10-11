# Abrir archivo
inputtxt = input("Nombre de archivo (con extensión): ")
if inputtxt == "fuck u":
    print("no u")
    exit()
try:
    fileh = open(inputtxt, "r")
except:
    print("Haga eso bien")
    exit()

# Ejercicio 1
codic = {}
midic = {}
for line in fileh:
    if not line.startswith("From") or line.startswith("From:"):
        continue
    line.rstrip()
    linea = line.split()
    midic[linea[2]] = midic.get(linea[2], 0) + 1
    # EJ2
    codic[linea[1]] = codic.get(linea[1], 0) + 1

print(midic, "\n")
print(codic, "\n")

# Ejercicio 3
valores = list(codic.values())
llaves = list(codic.keys())
print(llaves[valores.index(max(valores))], max(valores), "\n")

# Ejercicio 4
dodic = {}
for line in fileh:
    if not line.startswith("From") or line.startswith("From:"):
        continue
    line.rstrip()
    linea = line.split()
    remi = linea[1].split("@")
    dodic[remi[1]] = dodic.get(remi[1], 0) + 1

print(dodic, "\n")