datos = [10,9,8,7,6,5,4,3,2,1,0]

dato = 6
# Búsqueda secuencial
for i in datos:
    if dato == i:
        print('encontrado')
    if i<dato:
        break
    print('buscando')

# Búsqueda binaria
# [10, 9, 8, 7, 6] [5, 4, 3, 2, 1]
# [10, 9, 8, 7, 6]
# [10, 9, 8] [7, 6]
# [7, 6]
# [7] [6]
# [6]
def particion(arr, valor,lim_inf, lim_sup):
    pivote = (lim_inf + lim_sup) // 2
    print('buscando binario')
    if arr[pivote]<valor:
        pivote = pivote // 2
        particion(arr, valor, lim_inf, pivote)
    elif arr[pivote] > valor:
        pivote = (len(arr) + pivote) // 2
        particion(arr, valor, pivote, lim_sup)
    else:
        print('encontrado')

particion(datos, dato, 0, len(datos))

# Búsqueda directa
# Hash / Índice
datos_ordenados = {}
for i in datos:
    datos_ordenados[i] = i
if datos_ordenados[dato]:
    print('encontrado')
# Hash
# 20 datos
# 10 posiciones
# 0 1 2 3 4 5 6 7 8 9
# 1 6 9 4 3 2 5 7 10 15 11 13 ...
# K mod N + 1
# Cubetas
datos_a_hashear = [1,6,9,4,3,2,5,7,10,15,11,13, 5, 41, 8, 99, 101,23]
datos_ordenados = {}
datos_char = ['hola','mundo', 'jose','victor']
centro = len(datos_char) // 2  
hash = (centro + (centro - 1)) + ord(datos_char[centro])
for i in datos_a_hashear:
    hash = i % 10 + 1
    if datos_ordenados.get(hash):
        datos_ordenados[hash].append(i)
    else:
        datos_ordenados[hash] = [i]
hash = 41 % 10 + 1

print(datos_ordenados.get(hash))