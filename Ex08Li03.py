idade = int(input("Tem quantos anos nadador?\n"))

if (idade < 5):
    print("Ainda não possui categoria na natação.")
elif ((idade >= 5) and (idade<= 7)):
    print(f"Sua categoria é infantil, pois sua idade é {idade}")
elif ((idade >= 8) and (idade<= 10)):
    print(f"Sua categoria é juvenil, pois sua idade é {idade}")
elif ((idade >= 11) and (idade<= 15)):
    print(f"Sua categoria é adolescente, pois sua idade é {idade}")
elif ((idade >= 16) and (idade<= 30)):
    print(f"Sua categoria é adulto, pois sua idade é {idade}")
else:
    print(f"Sua categoria é Senior, pois sua idade é {idade}")
