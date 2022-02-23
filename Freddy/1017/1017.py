kml = 12
time = int(input())
speed = int(input())
distance = time * speed
fuellspent = distance / kml 
print('{:.3f}'.format(fuellspent))