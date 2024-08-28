import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 3
soma = 0

for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    soma = soma + nota
media = soma / QUANTIDADE_NOTAS    

if nota >= 7:
    print("Aprovado")
elif nota >= 4:
    print("recuperação")
else:
    print("Reprovado")

print("===FIM===")         
       