N = input()
arr = []
unlucky = False
for each in N:
    arr.append(each)
for k in range(len(arr)):
    for i in arr:
        if arr[k] == '1':
            for l in range(len(arr)):
                for j in N:
                    if arr[l] == '3' and arr[k + 1] == arr[l]:
                        unlucky = True
if unlucky:
    print('{} es de Mala Suerte'.format(N))
else:
    print('{} NO es de Mala Suerte'.format(N))