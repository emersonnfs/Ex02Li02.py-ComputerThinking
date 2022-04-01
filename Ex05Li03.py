d = float(input("Informe quantos dias úteis tem no mês: "))
h = float(input("Informe quantas horas foram trabalhadas no mês: "))
s = float(input("Informe o seu salário por hora:R$ "))

h0 = d * 8
hx = h - h0
s0 = h0 * s
sx =  s * hx * 1.5
sf = sx + s0

if (h > h0):
    print("Sua hora-extra foi R$ {:.2f}".format(sx))
    print("E seu salário foi de R$ {:.2f}".format(sf))
else : 
    print("O salário padrão R${:.2f}".format(s0))