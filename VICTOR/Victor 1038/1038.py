X, Y = input().split()
X = int(X)
Y = int(Y)
store = {1: {'Name': 'Cachorro Quente', 'Price': 4.00},
        2: {'Name': 'X-Salada', 'Price': 4.50}, 
        3: {'Name': 'X-Bacon', 'Price': 5.00}, 
        4: {'Name': 'Torrada Simples', 'Price': 2.00}, 
        5: {'Name': 'Refrigerante', 'Price': 1.50}}

print('Total: R$ {:.2f}'.format(store[X]['Price'] * Y))