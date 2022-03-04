datos = [1,9,3,2,5,6,10]

minimo = 0
for i in range(0,datos):
    minimo = i
    for j in range(i + 1,len(datos)):
        if datos[minimo] > datos[j]:
            minimo = j
    temp = datos[minimo]
    datos[minimo] = datos[i]
    datos[i] = temp