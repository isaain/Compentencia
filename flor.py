def crecimiento(dias):
    contador = 0
    crecer = 1
    while(contador < len(dias)):

        if dias[contador] == 1:
            
            if contador > 0:
                if dias[contador-1] == 1:
                    crecer+=5
                else:
                    crecer+=1
            else:
                crecer += 1

        elif contador > 0:
            if dias[contador] == 0 and dias[contador-1] == 0:
                #muere
                return -1
        contador+=1

    return crecer


cantidad_de_flores = int(input())
respuesta = []
for i in range(0, cantidad_de_flores):
    n,dias = int(input()), list(map(int,input().split()))
    respuesta.append(crecimiento(dias))

for k in range(0,len(respuesta)):
    print(respuesta[k])
