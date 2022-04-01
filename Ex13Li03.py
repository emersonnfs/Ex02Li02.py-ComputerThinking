dia = int(input("Informe que dia do mês é: "))
mes = int(input("Informe qual mês é de (1 a 12): "))

if ((dia > 31) or (dia < 1) or (mes < 1) or (mes > 12)):
    print("Data inválida.")
elif ((dia > 30) and ((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11))):
    print("Data inválida.")
elif ((dia > 28) and (mes == 2)):
    print("Data inválida.")
else:
    print(f"Data válida: \n{dia} / {mes}")