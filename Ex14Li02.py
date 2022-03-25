cheio = float(input("Informe o valor a vista do IPTU: R$"))

prazo = float(input("Informe o valor das parcelas do IPTU: R$"))

porcentagem = (1 - (cheio / (prazo * 10))) * 100

porcentagem = float(porcentagem)

print("O desconto foi", porcentagem, "%")