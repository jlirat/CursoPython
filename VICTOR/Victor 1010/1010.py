
# -*- coding: utf_8 -*-
code,unit,price = input().split()
code2,unit2,price2 = input().split()

PAGAR = int(unit) * float(price) + int(unit2) * float(price2)
print('VALOR A PAGAR: R$ {:.2f}'.format(PAGAR))