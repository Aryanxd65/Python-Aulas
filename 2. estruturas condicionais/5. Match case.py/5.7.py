import os
os.system("cls || clear")

altura = float(input("Digite sua altura: "))

sexo = input("escolha seu sexo: ")

match (sexo):
    case "M":
        peso_ideal = (72.7 * altura) - 58
        print(f"Peso ideal: {peso_ideal:.2f}KG") 
    case "F" :
        peso_ideal = (62.1 * altura) - 44.7
        print(f"Peso ideal: {peso_ideal:.2f}KG")