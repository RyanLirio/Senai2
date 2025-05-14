latinha = int(input("Insira quantas latinhas de 350ml voce deseja comprar: "))
garrafinha = int(input("Insira quantas garrafas de 600ml voce deseja comprar: "))
garrafa = int(input("Insira quantas garrafas de 2L voce deseja comprar: "))

latinha /= 1000
garrafinha /= 1000

Litros = garrafinha + latinha + garrafa

print(f"A quantidade em L compradas foram: {Litros:.2f}") 