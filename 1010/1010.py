total = 0
for contador in range(1,2):
    code, cant, precio = input().split()
    # code = entrada[0]
    cant = int(cant)
    precio = float(precio)
    resultado = cant * precio
    total = total + resultado # N veces

print('VALOR A PAGAR: R$ {0:.2f}'.format(total))