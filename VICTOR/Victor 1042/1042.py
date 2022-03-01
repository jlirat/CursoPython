arr = input().split()
numberarr = []
for item in arr:
    numberarr.append(int(item))
for i in sorted(numberarr):
    print(i)
print('')
for j in arr:
    print(j)