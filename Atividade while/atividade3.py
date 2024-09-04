import os
os.system("cls || clean")

# Solicita o número inicial ao usuário
numero_inicial = float(input("Digite o número inicial: "))

# Solicita o fator de multiplicação ao usuário
fator = float(input("Digite o fator de multiplicação: "))

# Inicializa o produto com o número inicial
produto = numero_inicial

# Inicializa o contador de multiplicações
multiplicacoes = 0

# Loop até que o produto exceda 100
while produto <= 100:
    produto *= fator
    multiplicacoes += 1

# Exibe o produto final e o número de multiplicações realizadas
print(f"O produto final é: {produto}")
print(f"Número de multiplicações realizadas: {multiplicacoes}")