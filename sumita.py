n = int(input())
suma = 1
for i in range(0,n):
    suma += (1/(i+1))

print(round(suma-1,8))