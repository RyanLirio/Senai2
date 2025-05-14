altura_pessoa = float(input("Insira a altura da pessoa: "))
sombra_pessoa = float(input("Insira o tamanho da sombra que essa pessoa faz: "))
sombra_predio = float(input("Insira o tamanho da sombra que o predio faz: "))

altura_predio = (altura_pessoa * sombra_predio) / sombra_pessoa
print(f"A altura do predio eh: {altura_predio}")