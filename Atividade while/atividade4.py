import os
os.system("cls || clear")


gasto_total = 0

orcamento = float(input("Digite seu orçamento: "))

while gasto_total <= orcamento:
        gasto_diario = float(input("Digite quantas hrs foram gastas: "))

        gasto_total += gasto_diario

        if gasto_total > orcamento:
            break

excedente = orcamento - gasto_total



print(f"Valor excedente: {excedente}")
print(f"Valor total gasto: {gasto_total}")
