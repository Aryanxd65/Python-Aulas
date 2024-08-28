import os
import time

os.system("cls || clear")
print("Laço de repetição - For")

numero = int(input("Digite um numero: "))

 
for i in range(numero,0,-1):
    print(f"Contagem Regressiva = {i}")
    time.sleep(2) # Vai esperar 2 segundos.

print("===FIM===")   