# Leitura das notas
nota1 = float(input("Digite a primeira nota:9 "))
nota2 = float(input("Digite a segunda nota:8 "))
nota3 = float(input("Digite a terceira nota:8 "))

# Pesos fixos
peso1, peso2, peso3 = 2, 3, 5

# Cálculo da média ponderada
media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# Exibição do resultado
print(f"A média ponderada é: {media:.2f}")
