ano_nascimento = int(input("Insira o ano do seu nascimento: "))
ano_hoje = int(input("Insira o ano em que estamos: "))
ano = ano_hoje - ano_nascimento
print(f"Você tem {ano} anos de vida desde que nasceu")

mes = ano * 12
print(f"Voce tem {mes} meses de vida desde que nasceu")

dia = mes * 30
print(f"Você tem {dia} dias de vida desde que nasceu")

semana = dia / 7 
print(f"Você tem {semana:.2f} semanas de vida desde que nassceu")