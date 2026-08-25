a,b,c = map(int,input().split())
resta = b - a
if resta % c == 0:
    print("S")
else:
    print("N")