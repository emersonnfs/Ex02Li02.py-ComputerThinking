aluno = int(input("Informe quantas aulas você compareceu: ")) 
aula = int(input("Informe quantas aulas teve no semestre: "))

presenca = aluno / aula

if (presenca >= 0.7):
    s1 = float(input("Informe a sua média do primeiro semestre: "))
    s2 = float(input("Informe a sua média do segundo semestre: "))
    
    media = (s1 * 0.4) + (s2 * 0.6)
    
    if (media >= 6):
        print("Parabens você passou !!!!! \nSua media foi {:.2f}" .format(media))
    else :
        print("Você está de Exame. \nSua média foi {:.2f}" .format(media))
else :
    print(f"Você foi REPROVADO, não teve presença superior a 70%. \nSua presença foi de {presenca * 100}%")