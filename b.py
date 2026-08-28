#B
n = int(input())
respuesta = 0
numeros = list(map(int,input().split()))
numeros.sort()

if n % 2 != 0:
  respuesta = numeros[(n//2)]
else:
  respuesta = numeros[(n//2)-1]

print(respuesta)
