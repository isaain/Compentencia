n = int(input())
divisores = list(map(int,input().split()))
if(divisores[0] == 1):
    print("*")
else:
    maximo = max(divisores)

    divisores.pop(divisores.index(maximo))
    divisores.pop(divisores.index(1))
    i = 0
    respuesta = 0
    for divisor in divisores:

        if maximo % divisores[i] == 0:
            respuesta = maximo
            break
        else:
            maximo = maximo * 2
            if maximo % divisores[i] == 0:
                respuesta = maximo
                break
        i += 1
    divisores.append(maximo)
    if respuesta != 0:
        if respuesta not in divisores:
            print(f"{respuesta} {respuesta}")
        else:
            #buscar todos los divisores n menos el maximo del maximo
            for i in range(1,maximo):
                if maximo % i == 0 and i not in divisores:
                    respuesta2 = i
                    break
            print(f"{respuesta} {respuesta2}")

    else:
        print("*")
