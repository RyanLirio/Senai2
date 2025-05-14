horas_normais = float(input("Insira a quantidade de horas trabalhadas normais: "))
horas_extras = float(input("Insira a quantidade de horas extras trabalhadas: "))

horas_normais *= 10
horas_extras *= 15

salario_bruto = horas_extras + horas_normais
desc = salario_bruto * 0.1 
salario_liquido = salario_bruto - desc

print(f"Você recebeu R${horas_normais:.2f} por suas horas normais\nR${horas_extras:.2f} por suas horas extras\nSeu salario bruto foi de: R${salario_bruto:.2f}\nCom um total de desconto de 10% sobre isso que deu: R${desc:.2f}\nSeu salario líquido é: R${salario_liquido} ")