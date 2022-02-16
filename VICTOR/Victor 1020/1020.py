tiempo = int(input())

anos = tiempo//365
tiempo -= anos*365
meses = tiempo//30
tiempo -= meses*30

print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(anos,meses,tiempo))