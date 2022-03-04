datos = [10,9,8,7,6,5,4,3,2,1]

# Ordenar
# Recorrer la lista
# for i in range(0,len(datos)):
#     min = i
#     for j in range(i+1, len(datos)):
#         if datos[min] > datos[j]:
#             min = j
#         print(datos)
#     temp = datos[min]
#     datos[min] = datos[i]
#     datos[i] = temp

# for i in range(0, len(datos)):
#     for j in range(i+1, len(datos)):
#         if datos[i] > datos[j]:
#             temp = datos[i]
#             datos[i] = datos[j]
#             datos[j] = temp

# min = 0
# [1, 9, 3, 2, 5, 6, 10]


# [10,9,8,7,6,5,4,3,2,1]
# [6,5,4,3,2,][1,10,9,8,7]
# [1,6,5,3,2,9,8,7]
# QuickSort
def particion(k, low, high):
    pivot= k[high]

    i = low - 1
    for j in range(low, high):
        if k[j] <= pivot:
            i = i + 1
            temp = k[i]
            k[i] = k[j]
            k[j] = temp
    (k[i+1], k[high]) = (k[high], k[i+1])
    print(k)
    return i + 1

def quicksort(k, low, high):
    if low < high:
        pi = particion(k, low, high)
        quicksort(k, low, pi-1)
        quicksort(k, pi + 1, high)

quicksort(datos, 0, len(datos)-1)
print(datos)

datos.sort()
