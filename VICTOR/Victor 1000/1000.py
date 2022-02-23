# N = input()
# unlucky = False
# count = 0
# while len(N) - 1 > count:
#     if N[count] == '1':
#         if N[(count + 1)] == '3':
#             unlucky = True 
#     count += 1
# if unlucky:
#     print('{} es de Mala Suerte'.format(N))
# else:
#     print('{} NO es de Mala Suerte'.format(N))
num = input()
i = 0
esDeMalaSuerte = False
while esDeMalaSuerte != True and i <= len(num):
    if num[i] == "1" and num[i + 1] == "3":
        esDeMalaSuerte = True
    i += 1
if esDeMalaSuerte:
    print('{} es de Mala Suerte'.format(num))
else:
    print('{} NO es de Mala Suerte'.format(num))