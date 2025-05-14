peso = float(input("Insira seu peso: "))
gordo = peso + (peso * 0.15)
magro = peso - (peso * 0.2)

print(f"Se adicionarmos 15% ao seu peso: {gordo:.2f}Kg\nE se subtrairmos 20% do seu peso: {magro:.2f}Kg")