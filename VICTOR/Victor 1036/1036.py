import math
A,B,C = input().split()
A = float(A)
B = float(B)
C = float(C)
if A == 0:
    print('Impossivel calcular')
else:
    try:
        Bhaskara1 = (-B + math.sqrt(B**2 - 4*A*C))/(2*A)
        Bhaskara2 = (-B - math.sqrt(B**2 - 4*A*C))/(2*A)
    except ValueError or ZeroDivisionError:
        print('Impossivel calcular')
    else:
        print('R1 = {:.5f}\nR2 = {:.5f}'.format(Bhaskara1,Bhaskara2))
