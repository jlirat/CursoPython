x = int(input())
X = x
notade100 = x//100
x -= notade100 * 100
notade50 = x//50
x -= notade50 * 50
notade20 = x//20
x -= notade20 * 20
notade10 = x//10
x -= notade10 * 10
notade5 = x//5
x -= notade5 * 5
notade2 = x//2
x -= notade2 * 2
notade1 = x//1
x -= notade1

print('{}\n{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00'.format(
    X, notade100,notade50,notade20,notade10,notade5,notade2,notade1))