started,ended = input().split()
started = int(started)
ended = int(ended)
count = 0
if started == ended:
    for i in range(0,24):
        count += 1
elif started > ended:
    for i in range(started , 24 + ended):
        count += 1
elif ended > started:
    for i in range(started, ended):
        count += 1

print('O JOGO DUROU {} HORA(S)'.format(count))