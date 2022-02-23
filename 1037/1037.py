value = float(input())

if value<0.00 or value>100:
    print("Fora de intervalo")
elif value >= 0.00 and value <=25:
    print("Intervalo [0,25]")
elif value > 25.00000 and value <= 50.00000:
    print("Intervalo (25,50]")
elif value > 50.00000 and value <=75.00000:
    print("Intervalo (50,75]")
elif value > 75.00000 and value <=100.00000:
    print("Intervalo (75,100]")
