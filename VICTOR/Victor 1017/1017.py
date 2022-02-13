kmL = 12
spentTime = int(input())
averageSpeed = int(input())
Distance = spentTime * averageSpeed
fuelSpent = Distance / kmL
print('{:.3f}'.format(fuelSpent))