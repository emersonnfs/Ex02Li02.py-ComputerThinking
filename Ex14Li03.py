dia = int(input("Informe que dia do mês é: "))
mes = int(input("Informe qual mês é de (1 a 12): "))
ano = int(input("Informe qual o ano: "))

if dia > 31 or dia < 1 or mes < 1 or mes > 12:
    print("Data inválida.")
elif dia > 30 and mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("Data inválida.")
elif dia > 29 and mes == 2:
    print("Data inválida.")
elif mes != 2:
    print(f"Data válida: \n{dia}/{mes}/{ano}")
elif mes == 2 and ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0 : 
    print(f"Data válida: \n{dia}/{mes}/{ano}")
else :
    print("Data Inválida.") 