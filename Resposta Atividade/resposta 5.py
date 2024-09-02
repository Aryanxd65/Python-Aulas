
import os
os.system("cls || clear")

#solicitando dados
numero = int(input("Digite o valor que quer mutiplicar de 1 á 6: "))

for i in range(1,7):
    print(f"{i} x {numero} = {numero * i}")
