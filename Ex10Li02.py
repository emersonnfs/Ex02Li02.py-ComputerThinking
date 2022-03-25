tempo = float(input("Digite em quantos segundos foi percorridoa a distancia: "))

distancia = float(input("Digite a distância percorrida em metros: "))

velom = distancia / tempo

velok = velom * 3.6

print("A velocidade média, dado que percorreu", distancia, "metros, em", tempo, "segundos, foi de ", velom, "m/s, e ", velok, "Km/h")