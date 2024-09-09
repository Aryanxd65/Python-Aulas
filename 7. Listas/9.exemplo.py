import os
os.system("cls || clear")

# Função para calcular a idade
def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento  # Calcula a idade
    return idade

# Solicita o ano de nascimento ao usuário
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Solicita o ano atual ao usuário
ano_atual = int(input("Digite o ano atual: "))

# Chama a função e obtém a idade
idade = calcular_idade(ano_nascimento, ano_atual)

# Exibe a idade
print(f"A sua idade é: {idade} anos")