
lista = input().split() # [v1, v2, v3]
cont = 0
mayor = 0
greatest = 0
while cont < len(lista) - 1:
    a_string = lista[cont]
    a = int(a_string)
    b_string = lista[cont + 1]
    b = int(b_string)
    mayor = (a + b + abs(a - b)) / 2
    # mayor = (int(lista[cont]) + int(lista[cont+1]) + abs(int(lista[cont]) - int(lista[cont+1])))
    greatest = (greatest + mayor + abs (greatest - mayor)) / 2
    cont = cont + 1

print('{0:.0f} eh o maior'.format(greatest))

######
## 7 [14 106]
# cont = 0 
# => a = 7
# => b = 14
# mayor = 14
# cont = 1
# => a = 14
# => b = 106
# mayor = 106
# cont = 2
# 106 eh o maior
