X,Y = input().split()
X = float(X)
Y = float(Y)
if X == 0 and Y != 0:
    print('Eixo X')
elif X != 0 and Y == 0:
    print('Eixo Y')
else:
    try:
        X = X / abs(X)
        Y = Y / abs(Y)
        if X == 1 and Y == 1:
            print('Q1')
        if X == -1 and Y == 1:
            print('Q2')
        if X == -1 and Y == -1:
            print('Q3')
        if X == 1 and Y ==-1:
            print('Q4')
    except ZeroDivisionError:
        if X == 0 and Y == 0:
            print('Origem')

