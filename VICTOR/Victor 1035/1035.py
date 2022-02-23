A,B,C,D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)
val = False
if B > C and D > A and (C + D) > (A + B) and (C - C) == 0 and (D - D) == 0 and A % 2 == 0:
    val = True

if val == True:
    print("Valores aceitos")
else:
    print('Valores nao aceitos')