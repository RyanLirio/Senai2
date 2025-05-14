umcentavo = int(input("Insira a quantidade de moedas de 1 centavo tem no seu cofrinho: "))
cincocentavo = int(input("Insira a quantidade de moedas de 5 centavos tem no seu cofrinho: "))
dezcentavo = int(input("Insira a quantidade de moedas de 10 centavos tem no seu cofrinho: "))
vintecincocentavo = int(input("Insira a quantidade de moedas de 25 centavos tem no seu cofrinho: "))
cinquentacentavo = int(input("Insira a quantidade de moedas de 50 centavos tem no seu cofrinho: "))
umreal = int(input("Insira a quantidade de moedas de 1 real tem no seu cofrinho: "))

umcentavo *= 0.01
cincocentavo *= 0.05
dezcentavo *= 0.10
vintecincocentavo *= 0.25
cinquentacentavo *= 0.50

total = umcentavo + cinquentacentavo + cincocentavo + dezcentavo + vintecincocentavo + umreal

print(f"um centavo = R${umreal}\ncinco centavos = R${cincocentavo}\ndez centavos = R${dezcentavo}\nvinte e cinco centavos = R${vintecincocentavo}\ncinquenta centavos = R${cinquentacentavo}\num real = {umreal}\nTotal = R${total}")