N1,N2,N3,N4 = input().split()
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)
N1Weight = 2
N2Weight = 3
N3Weight = 4
N4Weight = 1
Media = (N1*N1Weight) + (N2*N2Weight) + (N3*N3Weight) + (N4*N4Weight) 
Media = int(Media)/10
print('Media: {:.1f}'.format(Media))
if Media >= 7.0:
    print('Aluno aprovado.')
elif Media < 5.0:
    print('Aluno reprovado.')
elif Media >= 5.0 and Media < 7.0:
    print('Aluno em exame.')
    mno = float(input())
    print('Nota do exame: {:.1f}'.format(mno))
    niu_media = (Media + mno)/2
    if niu_media >= 5.0:
        print('Aluno aprovado.')
    elif niu_media < 5.0:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(niu_media))
"""
78.85 -> 78.8
788.5
788
78.8
round(valor,digitos) -> Redondea 
int() -> Solo el entero
math.truncate() -> Solo el entero
"""