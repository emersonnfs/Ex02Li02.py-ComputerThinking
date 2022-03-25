preco = float(input("Informe o valor do produto:R$ "))

desconto = float(input("Informe qual o desconto em porcentagem: "))

desconto_real = 1 - (desconto / 100)

preco_final = preco * desconto_real

valor_desconto = preco * (desconto / 100)

print("O valor do desconto foi de R$", valor_desconto, ", e o preço com o desconto já aplicado é R$", preco_final)