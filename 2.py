import math
a= float(input("Digite o valor de a: "))
if a == 0:
    print("Essa equação não é do segundo grau!")
else:
    b= float(input("Digite o valor de b: "))
    c= float(input("Digite o valor de c: "))
    d = b**2 - (4*a*c)
    if d < 0:
        print("Não existem raizes reais!")
    else:
        r1 = (-b + math.sqrt(d))/(2*a)
        if d == 0:
            print("Raiz: %.3f" %r1)
        if d > 0:
            r2 = (-b - math.sqrt(d))/(2*a)
            print("Primeira raiz: %.3f" %r1)
            print("Segunda raiz: %.3f" %r2)