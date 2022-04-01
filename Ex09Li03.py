from statistics import multimode


n1 = float(input("Digite o primeiro número: "))
op = input("Digite o operador *;/;-;+ : ")
n2 = float(input("Digite o segundo número: "))

soma = n1 + n2
sub = n1 - n2
mult= n1 * n2
div = n1 / n2

if op == "+" :
    print(f"{n1} + {n2} = {soma}")
elif op == "-" :
    print(f"{n1} - {n2} = {sub}")
elif op == "*" :
    print(f"{n1} * {n2} = {mult}")
elif ((op == "/") and (n2 != 0)):
    print(f"{n1} / {n2} = {div}")
elif ((op == "/") and (n2 == 0)):
    print("Não tem divisão por 0.")
else:
    print("Não foi possível fazer a conta.")