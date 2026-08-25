import random
n = int(input())
arreglo = []
for i in range(0,n):
    arreglo.append(i+1)

random.shuffle(arreglo)
print(arreglo)