valor = float(input("Informe o valor do produto: R$"))
forma = float(input("Forma de pagamento;\nA vista no dinheiro ou cheque(com desconto de 10%). Digite 1 \nA vista no cartão(com desconto de 5 %). Digite 2 \nEm 2 vezes no cartão (sem juros). Digite 3 \nEm 4 vezes no cartão (com juros de 7%). Digite 4 \nQual sua forma de pagamento: "))

desc1 = valor * 0.9
desc2 = valor * 0.95
jur1 = valor * 1.07

if (forma == 1):
    print(f"R${desc1}")
elif (forma == 2):
    print(f"R${desc2}")
elif (forma == 3):
    print(f"R${valor}")
elif (forma == 4):
    print(f"R${jur1}")
else:
    print("Não está correta a informação de valor ou forma de pagamento")