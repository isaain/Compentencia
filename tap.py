palabraCompleta = input()
encontroP = False
encontroT = False
encontroA = False

for i in range(0,len(palabraCompleta)):
    if palabraCompleta[i] == "T":
        encontroT = True
    if palabraCompleta[i] == "A" and encontroT == True:
        encontroA = True
    if palabraCompleta[i] == "P" and encontroA == True and encontroT == True:
        encontroP = True

if encontroP == True:
    print("S")
else:
    print("N")