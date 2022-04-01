t1 = input("Qual o nome do primeiro time:")
t2 = input("Qual o nome do segundo time: ")

r1 = int(input("Quantos gols o primeiro time marcou"))
r2 = int(input("Quantos gols o segundo time marcou"))

if r1 > r2:
    print("O", t1,"venceu", t2)
elif r2 > r1:
    print("O", t2,"venceu", t1)
else:
    print("Foi empate")