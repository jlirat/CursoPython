def EsTriangulo(A,B,C):
    if (A + B) > C and (B + C) > A and (A + C) > B:
       return True
    else:
        return False 
    
def AreaTrapecio(BaseMenor,BaseMayor,Altura):
    Bases = BaseMenor + BaseMayor
    Area = (Bases * Altura)/2
    return Area

def PerimetroTriangulo(A,B,C):
    Perimetro = A + B + C
    return Perimetro
A,B,C = input().split()
A = float(A)
B = float(B)
C = float(C)
if EsTriangulo(A,B,C):
    Perimetro = PerimetroTriangulo(A,B,C)
    print('Perimetro = {:.1f}'.format(Perimetro))
else:
    Area = AreaTrapecio(A,B,C)
    print('Area = {:.1f}'.format(Area))