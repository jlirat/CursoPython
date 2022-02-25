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

# s = input()
# new_s = ''
# for c in s:
#     new_c = ord(c) + 3
#     print("\{}".format(new_c))
#     new_s+=chr(ord(c)+3)
# print(new_s)

lista = [x * 2 for x in range(1,10)]


