H1,M1,H2,M2 = input().split()
H1 = int(H1)
H2 = int(H2)
M1 = int(M1)
M2 = int(M2)
M1 += H1*60
M2 += H2*60
Time = 0
if M1 == M2:
    for i in range(0,1440):
        Time += 1
elif M1 > M2:
    for i in range(M1, 1440 + M2):
        Time += 1
elif M2 > M1:
    for i in range(M1, M2):
        Time += 1
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(Time//60,(Time - (Time//60)*60)))

    