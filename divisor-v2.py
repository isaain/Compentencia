import math
n = int(input())
numeros = list(map(int,input().split()))
if numeros[0] == 1 and n == 1:
    print("*")
else:
    primer_res = math.lcm(*numeros)
    resultado2 = 0
    encontro = False

    if primer_res in numeros:
        raiz_cuadrada = math.isqrt(primer_res)
        #voy de 2 hasta la raiz cuadrada del mcm que esta en el arreglo
        for i in range(2,raiz_cuadrada):

            if primer_res % i == 0:

                if i not in numeros:
                    resultado2 = i
                    encontro = True
                    break
                #si ese divisor divide al mcm ya lo encuentra
                if primer_res // i not in numeros:
                    resultado2 = primer_res//i
                    encontro = True
                    break
        if encontro == False:
                print("*")
        else:
                print(f"{primer_res} {resultado2}")
    else:
        print(f"{primer_res} {primer_res}")
