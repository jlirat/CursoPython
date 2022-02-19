A,B,C = input().split()
A = float(A)
B = float(B)
C = float(C)
artr = A * C/2.0
Pi = 3.14159
arcr = Pi * C**2.0
artrap = ((A + B) * C)/2
arsq = B**2.0
arrct = A * B
print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO {:.3f}\nQUADRADO {:.3f}\nRECTANGULO: {:.3f}'.format(artr,arcr,artrap,arsq,arrct))