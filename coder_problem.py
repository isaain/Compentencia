n = int(input())
if n % 2 == 0:
    coders = (n*n)//2
else:
    coders = ((n*n)//2)+1
print(coders)
# matriz
matriz = [['valor_de_inicializacion' for t in range(n)] for w in range(n)]

for i in range(0,n):
    for j in range(0,n):
        if i == 0 or i % 2 == 0:
            if j == 0 or j % 2 == 0:
               matriz[i][j] = 'C'

        else:
            if j % 2 != 0:
                matriz[i][j] = 'C'
    
for v in range(0,n):
    print(''.join(matriz[v]))