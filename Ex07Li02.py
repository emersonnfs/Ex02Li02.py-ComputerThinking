numero = int(input("Digite um número inteiro de 0 a 99: "))

unidade = numero % 10

numero = ( numero - unidade ) / 10

dezena = numero

dezena = int(dezena)

print('o número tem', dezena ,'dezena(s) e ', unidade , 'unidade(s)')