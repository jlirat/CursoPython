v = float(input())
# coins = [1.0, 0.50, 0.25, 0.10, 0.05, 0.01]
# notas = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0]
notas = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.50, 0.25, 0.10, 0.05, 0.01]

# notes = {}
# moedas = {}

if (0.00 <= v <= 1000000.00):
    print('NOTAS:')
    band = False
    for n in notas:
        if n < 2 and band == False:
            print('MOEDAS:')
            band = True
        p1 = v // n
        v = round(v % n, 2)
        
        # notes[n] = int(p1)
        # p1 = int(p1)
        print('{0:.0f} nota(s) de R$ {1:.2f}'.format(p1, n))
    # for c in coins:
    #     p1 = v / c
    #     v = v % c
    #     print(v)
    #     # moedas[str(c)] = int(p1)
    # print('NOTAS:')
    # for n in notas:
    #     print('{0:.0f} nota(s) de R$ {1:.2f}'.format(notes[n], n))
    # print('MOEDAS:')
    # for c in coins:
    #     print('{0:.0f} moeda(s) de R$ {1:.2f}'.format(moedas[str(c)], c))
