N = input()
number = 0
count = 0
arr = []
while 14 > count:
    if N[count] == '1' or N[count] == '2' or N[count] == '3' or N[count] == '4' or N[count] == '5' or N[count] == '6' or N[count] == '7' or N[count] == '8' or N[count] == '9' or N[count] == '0':
        arr[count].append(N[count])
    count += 1
print(arr)