salario = float(input("Insira o seu salario: R$"))
vendas = float(input("Insira o valor de suas vendas: R$"))

salario += vendas * 0.04

print(f"seu salario mais 4% de comissao sobre suas vendas: R${salario}\nForam adicionados R${vendas * 0.04} de comissoes")