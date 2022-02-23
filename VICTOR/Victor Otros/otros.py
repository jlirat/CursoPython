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
N = int(input())
count = N
str1 = ''
while N != 0:
    if N % 2 == 0:
        str1 = '0' + str1
        N = N//2
    elif N % 2 != 0:
        str1 = '1' + str1
        N = N//2
    count += 1
print(str1)