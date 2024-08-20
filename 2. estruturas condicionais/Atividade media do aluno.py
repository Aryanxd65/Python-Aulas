import os
os.system("cls || clear")


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

nota1 = float(input("Digite aqui a primeira nota: "))
nota2 = float(input("Digite aqui a segunda: "))
nota3 = float(input("Digite aqui a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Nome: {nome}. ")
print(f"idade: {idade} anos.")
print(f"Média: {media} ")

if media < 7:
    print ("ALUNO REPROVADO")
else:
    print("ALUNO APROVADO")    
