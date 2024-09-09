import os
os.system("cls || clear")

def verificar_pares_impares():
    pares = 0
    impares = 0


    for i in range(6):
        numero = int(input("Digite um número: "))

        if numero % 2 == 0:
            pares += 1 
        else:
            impares
                


print(f"\nQuantidade pares: {pares}")
print(f"Quantidade ímpares: {impares}")    