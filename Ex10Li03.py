import math

a =int(input("Dado a função ax2 + bx + c = 0. \nInforme o valor de a: "))
b =int(input("Informe o valor de b: "))
c =int(input("Informe o valor de c: "))

delta = ((b * b) - (4 * a * c))
x1 = (((-b) + math.sqrt(delta)) /(2 * a) )
x2 = (((-b) - math.sqrt(delta)) /(2 * a) )

if ((a != 0) and (math.sqrt(delta) // 1 == math.sqrt(delta))):
    print(f"As raizez da equação são {x1} e {x2}")
else : 
    print("As raizes da equação não são reais")