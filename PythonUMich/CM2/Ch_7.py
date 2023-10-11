import numpy as np

# Ejemplo 1
inputtxt = input("Nombre de archivo (con extensión): ")

if inputtxt == "fuck u":
    print("no u")
    exit()

try:
    ahandle = open(inputtxt, "r")
except:
    print("Ale bien")
    exit()

for line in ahandle:
    lp = line.upper()
    print(lp.rstrip())

# Ejercicio 2
spaml = []
for line in ahandle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    lst = line.find("X-DSPAM-Confidence: ")
    nst = line.find(" ", lst)
    nen = line.find("\n", nst)
    spaml.append(float(line[nst+1:nen]))
print(np.mean(spaml))