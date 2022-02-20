v = float(input())
notas = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0]
coins = [1.0, 0.50, 0.25, 0.10, 0.05, 0.01]

notes = {}
moedas = {}
if (0.00 <= v <= 1000000.00):
    for n in notas:
        p1 = v / n
        # v = v - (p1 * n)
        v = v % n
        notes[n] = int(p1)
    for c in coins:
        p1 = v / c
        # v = v - (p1 * c)
        v = v % c

        moedas[str(c)] = int(p1)
    print('NOTAS:')
    for n in notas:
        print('{0:.0f} nota(s) de R$ {1:.2f}'.format(notes[n], n))
    print('MOEDAS:')
    for c in coins:
        print('{0:.0f} moeda(s) de R$ {1:.2f}'.format(moedas[str(c)], c))
