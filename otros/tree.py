# print("\t*")
# print("    **")
# print("\t***")
# print("    ****")
# print("\t*****")
# print("    ******")

# |0|0|1|0
# |0|1|0|0
#  0  1  1  0
#  0  4  2  0 = 6
#  0  0  0  0 = 0

# 1
# 1 0 0 0 0 0
# 0 0000000 00000000 00000000 00000000
# 0 000000 00000000 00000000 00000000
# S 
# 0 0000000
# 0 0000000
# 1 0000000
# 1 0000001 
# 0
# 1
#...
# 255

# x = 2
# y = 2.0
# z = False
# w = "Hello"
# a = "World"
# b = "!"
# c = 4
# d = 1
# resultado  = x and z # or ||
# resultado2 = x + y
# resultado3 = x & c

# resultado4 = d << 5

# # for x in range(2,2,2,2,2):
# #     d*=x    
# print(resultado4)

# Hacer un programa que determine si un número es par o impar
# 111001
# 000001
# 000001 = 1
# 110000
# 000011
#=000000 = 0

# num = int(input())

# if (num & 1)==0:
#     print('par')
# else:
#     print('impar')

# cad = "cadena"
# otra_cadena = 'otra_cadena'
# esta_cadena = "\"cadena\" y \"otra_cadena\" \t\r\n"
# numero1 = str(10)
# numero2 = str(11)
# especial = f"10 + 11 = {10 + 11}"
# longitud = len(especial)
# print(cad)
# print(otra_cadena)
# print(numero1 + numero2)
# print(longitud)
# print(especial)
# print(esta_cadena)
# print(esta_cadena[3:5].upper())
# print(esta_cadena[3:5].lower())
#Conjetura de Collatz



def TresNMasUno(N,secuencia):
        if N & 1 == 1:
            N = N*3 + 1
            secuencia.append(N)
            return N,secuencia
        else:
            N = N>>1
            secuencia.append(N)
            return N,secuencia
N = int(input())
secuencia = []
while N != 1:
    N,secuencia = TresNMasUno(N,secuencia)
    long = len(secuencia)
print(long)
# s = input()
# new_s = ''
# for c in s:
#     new_c = ord(c) + 3
#     print("\{}".format(new_c))
#     new_s+=chr(ord(c)+3)
# print(new_s)

# Criba de eratóstenes
# N = int(input())
# 1 2 3 4* 5 6* 7 8* 9* 10* 11 12* 13 14* 15* 16* 17 18* 19 20*
# 2 3 5 7 11 13 17 19
# lista = [False for x in range(0,N+1)] # Listas por comprensión

# print(lista)
# lista2 = []
# for i in range(2, N+1):
#     if lista[i]==False:
#         lista2.append(i)
#         p = i + i
#         while p <= N:
#             lista[p] = True
#             p+=i
# print(lista2)

# Si el número es impar entonces vamos a aplicar 3*n + 1
# Si el número es par entonces vamos a aplicar n / 2
# 5 => 3 * 5 + 1 = 16 => 8 => 4 => 2 => 1
# 10110 >> 1 => 1011
# f(x) = 0
def tresNMasUno(N):
    if N & 1 == 1:
        return 3 * N + 1
    else:
        return N >> 1


# [False, False, False, False, False]
#    0      1       2     3      4
#    1      2       3     4      5
# # Funciones
# value = int(input())

# while value!=1:
#     value = tresNMasUno(value)
#     print(value)

# def precio_total(c, p):
#     return c*p

# def leer():
#     (codigo, cantidad, precio) = input().split()
#     cantidad = int(cantidad)
#     precio = float(precio)
#     return (codigo, cantidad, precio)

# # total de costos cantidad precio código
# (codigo, cantidad, precio) = leer()
# total = precio_total(c = cantidad, p = precio)
# (codigo, cantidad, precio) = leer()
# total += precio_total(c = cantidad, p= precio)
# print(total)

# def func(N, secuencia):
#     if N & 1 == 1:
#         return N * 3 + 1
#     else:
#         return N>>1

value = int(input())
notes = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00]

print(value)

for i in notes:
    minimum = value // i
    value = value % i
    if value < .01:
        value = round(value, 2)
    print("{0:.0f} nota(s) de R$ {1:.2f}".format(minimum, i).replace('.',','))
