import os
os.system("cls || clear")

def calcular_media(nota1, nota2):
    """Calcula a média de duas notas."""
    return (nota1 + nota2) / 2

def verificar_aprovacao(media):
    """Verifica se a média é suficiente para aprovação."""
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Leitura das notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média
media = calcular_media(nota1, nota2)

# Verificação da aprovação
resultado = verificar_aprovacao(media)

# Exibição dos resultados
print(f"A média do aluno é: {media:.2f}")
print(f"O aluno está: {resultado}")