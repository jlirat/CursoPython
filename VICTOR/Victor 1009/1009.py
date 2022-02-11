# -*- coding: utf-8 -*-
NAME = input()
SALARY = float(input())
SALES = float(input())
BONUS = SALES *0.15
print('TOTAL = R$ {:.2f}'.format(SALARY + BONUS))