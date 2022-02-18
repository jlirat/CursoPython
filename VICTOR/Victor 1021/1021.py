dinheiro = float(input())
notade100 = dinheiro//100
dinheiro -= notade100 * 100
notade50 = dinheiro//50
dinheiro -= notade50 * 50
notade20 = dinheiro//20
dinheiro -= notade20 * 20
notade10 = dinheiro//10
dinheiro -= notade10 * 10
notade5 = dinheiro//5
dinheiro -= notade5 * 5
notade2 = dinheiro//2
dinheiro -= notade2 * 2
# monedas
moeda1 = dinheiro//1
dinheiro -= moeda1*1
moedamed = dinheiro//0.50
dinheiro -= moedamed*0.5
moedaquarter = dinheiro//0.25
dinheiro -= moedaquarter*0.25
moedadies = dinheiro//0.10
dinheiro -= moedadies*0.10
moedacinco = dinheiro//0.05
dinheiro -= moedacinco*0.05
moedaum = dinheiro//0.01
dinheiro -= moedaum*0.01
print('NOTAS:\n{:.0f} nota(s) de R$ 100.00\n{:.0f} nota(s) de R$ 50.00\n{:.0f} nota(s) de R$ 20.00\n{:.0f} nota(s) de R$ 10.00\n{:.0f} nota(s) de R$ 5.00\n{:.0f} nota(s) de R$ 2.00\nMOEDAS:\n{:.0f} moeda(s) de R$ 1.00\n{:.0f} moeda(s) de R$ 0.50\n{:.0f} moeda(s) de R$ 0.25\n{:.0f} moeda(s) de R$ 0.10\n{:.0f} moeda(s) de R$ 0.05\n{:.0f} moeda(s) de R$ 0.01'.format(notade100,notade50,notade20,notade10,notade5,notade2,moeda1,moedamed,moedaquarter,moedadies,moedacinco,moedaum))
