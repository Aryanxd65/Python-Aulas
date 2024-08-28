"""
escreva um algoritimo que solicite duas notas para um aluno.
Caso seja maior que 0 maior que 10, mostre a pergunta novamente.
Calcule e mostre a média aritmética do aluno
"""


import os
os.system ("cls || clean")
nota = 0

nota2 = 0


while True:
    nota = float(input("Digite a primeira nota : "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota + nota2) / 2

    if (nota < 0 or nota > 10) or (nota2 < 0 or nota > 10) :
        print("\nA nota deve ser maior ou igla a 0 e menor e igual  a 10.")
    else:
        break
 

print(f"Nota: {media}")        