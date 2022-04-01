a = int(input("Digite um número inteiro para saber se ele é divisível pelo segundo: "))
b = int(input("Digite um número inteiro para saber se ele divide: "))

c = a/b
r = a % b

if (r == 0):
    print(a,"é divisível por", b)
    print("Sua divisão é",c)
else: 
    print("Não é divisível")
