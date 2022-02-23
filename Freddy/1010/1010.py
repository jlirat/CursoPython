codigo,unidad,precio = input().split()
codigo2,unidad2,precio2 = input().split()
precios1= int(unidad) * float(precio)
precios2= int(unidad2) * float(precio2)
preciofinal = precios1 + precios2
print('VALOR A PAGAR: R$ {:.2f}'.format(preciofinal))