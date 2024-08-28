import os
os.system("cls || clear")

soma = 0



for i in range(3):
    nota = int(input(f"Digite  a {i+1}º  nota: "))
    soma = soma + nota
    

media = soma / 4
    



print(f"Média do aluno: {media}")