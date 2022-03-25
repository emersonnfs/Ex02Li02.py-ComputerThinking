numero = int(input("Digite o seu RM:"))

num5 = numero % 10

numero = (numero - num5) / 10
num4 = numero % 10

numero = (numero - num4) / 10
num3 = numero % 10

numero = (numero - num3) / 10
num2 = numero % 10

numero = (numero - num2) / 10
num1 = numero

soma = num1 +num2 + num3 + num4 + num5

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
num4 = int(num4)
num5 = int(num5)
soma= int(soma)

print("A soma do seu RM é: " + str(soma))