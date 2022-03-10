weights = [2.0,3.0,4.0,1.0]
ENES = input().split()
total = 0
    
for i in range(0, 4):
    total+=float(ENES[i]) * weights[i]

total = int(total) / 10

print("Media: {0:.1f}".format(total))
if total >= 7.0:
    print('Aluno aprovado.')
elif total < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exame = float(input())
    avg = (total + exame) / 2
    print('Nota do exame: {0:.1f}'.format(exame))
    if avg >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {0:.1f}'.format(avg))
    