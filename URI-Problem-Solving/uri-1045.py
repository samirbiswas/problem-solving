A, B, C = map(float, input().split())

if A >= (B + C):
    print("NAO FORMA TRIANGULO")
if A*A == ((B*B) + (C*C)):
    print("TRIANGULO RETANGULO")
if A*A > ((B*B) + (C*C)):
    print("TRIANGULO OBTUSANGULO")
if A*A < ((B*B) + (C*C)):
    print("TRIANGULO ACUTANGULO")
if A == B and C == A:
    print("TRIANGULO EQUILATERO")
if ((A == B) and A != C) or ((A == C) and A != B) or ((B == C) and B != A):
    print("TRIANGULO ISOSCELES")
