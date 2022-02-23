N = input()
clave = 18
count = 0
list = ''
while len(N) > count:
    orde = ord(N[count]) + 3
    list += chr(orde)
    count += 1
print(list)
