import os
os.system("cls || clear")

contagem_negativos = 0


while True:
    
    numero = float(input("Insira um número (0 ou positivo para parar): "))
    
    
    if numero >= 0:
        break
    
    
    contagem_negativos += 1

print(f"A quantidade de números negativos inseridos é: {contagem_negativos}")
