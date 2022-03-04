# numero par o impar
# numero = int(input())
# if numero & 1 == 0:
#     print('Tu numero es par')
# else:
#     print('Tu numero es impar')
# import random
# N = ''
# arr = ['Paco','Patricio','Pengo','Pepe','Diaz','Pato','Patricio','Pepito','Derivada','xd','no','ayno','quep','mno']
# while N == '' and arr != []:
#     N = input()
#     leng = len(arr)
#     ram = random.randint(0,leng - 1)
#     print(arr[ram])
#     arr.pop(ram)

# ENTERO A BINARIO-?
"""
256|128|64|32|16|8|4|2|1"""
# N = int(input())
# count = N
# str1 = ''
# while N != 0:
#     if N & 1 != 1:
#         str1 = '0' + str1
#         N = N//2
#     elif N & 1 == 1:
#         str1 = '1' + str1
#         N = N//2
#     count += 1
# while N != 0:
#     c = N & 1
#     N = N >> 1
#     str1 = str(c) + str1
# print(str1)
# str1 = 'hola'
# print(len(str1))
# cien = 100
# for i in range(0,cien + 1,2):
#     print(i)

# def range(x=0,y=0,z=1):
# N = input()
# count = 0
# suma = 0
# while N != '':
#     suma += int(N)
#     count += 1
#     N = input()
# promedio = suma/count
# print(promedio)
# n = int(input())
# count = 0
# listaDePrimos = []
# bandera = False
# while count <= n:
#     for i in range(2,count + 1,1):
#         if count % i == 0 and i != count:
#             bandera = False
#             break
#         else:
#             bandera = True
#     if bandera:
#         listaDePrimos.append(count)
#     count += 1
# print(listaDePrimos)
# numeroswao = [1,2,3,4,5,6,7,8,9,10]
# losprimos = []
# primo = False
# for n in numeroswao:
#     for i in range(2,n,1):
#         if n % i == 0:
#             break
#         else:
#             losprimos.append(n)

# print(losprimos)

