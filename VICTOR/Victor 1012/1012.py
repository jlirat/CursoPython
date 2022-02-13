A,B,C = input().split()
A = float(A)
B = float(B)
C = float(C)
rectangleTriangle = A * C/2.0
Pi = 3.14159
Circle = Pi * C**2.0
Trapezium = ((A + B) * C)/2
Square = B**2.0
Rectangle = A * B

print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'.format(rectangleTriangle,Circle,Trapezium,Square,Rectangle))