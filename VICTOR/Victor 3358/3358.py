def checarSiConsonante(letra):
    if letra[count] != 'a' and letra[count] != 'e' and letra[count] != 'i' and letra[count] != 'o' and letra[count] != 'u':
        if letra[count + 1] != 'a' and letra[count + 1] != 'e' and letra[count + 1] != 'i' and letra[count + 1] != 'o' and letra[count + 1] != 'u':
            if letra[count + 2] != 'a' and letra[count + 2] != 'e' and letra[count + 2] != 'i' and letra[count + 2] != 'o' and letra[count + 2] != 'u':
                return False
    else:
        return True
N = int(input())
Facil = True
for i in range(N):
    C = input()
    if len(C) < 42:
        count = 0
        while count < len(C)-2:
            C = C.lower()
            Facil = checarSiConsonante(C)
            count += 1
        if Facil:
            print('{} eh facil'.format(C.title()))
        else:
            print('{} nao eh facil'.format(C.title()))
            Facil = True