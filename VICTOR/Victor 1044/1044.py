def isMultiple(N,mul):
    if mul == N:
        return False
    elif mul % N == 0:
        return True
    else:
        return False
    
number,multiple = input().split()
number = int(number)
multiple = int(multiple)
if isMultiple(number,multiple):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')