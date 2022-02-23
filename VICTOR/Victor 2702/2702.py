count = 0
PlatosDis = input().split()
Pedidos = input().split()
Sobrantes = 0
while count < 3:
    if PlatosDis[count] < Pedidos[count]:
        Sobrantes -= int(PlatosDis[count]) - int(Pedidos[count])
    else:
        pass
    count += 1
print(str(Sobrantes))