import os
os.system("cls || clear")

soma = 0



for i in range(4):
    nota = int(input(f"Digite  a {i+1}º  nota: "))
    soma = soma + nota

media = soma / 4
    
if media >= 7:
        print("Aprovado!!!!")
else:
    print("Reprovado""")


print(f"Média do aluno: {media}")