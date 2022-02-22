A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)
MayorAB = ((A + B) + abs(A - B))/2
MayorABC = ((MayorAB + C) + abs(MayorAB - C))/2
print('{:.0f} eh o maior'.format(MayorABC))