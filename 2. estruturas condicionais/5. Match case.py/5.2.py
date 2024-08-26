import os
os.system("cls || clear")


print("""
1 - Picanha  
2 - Lasanha
3 - Strogonoff    
4 - Bifé acebolado
5 - Pão com ovo                       
      """)
opcao = int(input("Digite uma opção: "))

match(opcao):
    case 1:
        print("Picanha / R$ 25,00 ")
    case 2:
        print("Lasanha / 20,00 ")
    case 3:
        print("Strogonoff / 18,00  ")
    case 5:
        print("Bifé acebolado / 15,00 ")
    case 5:
        print("Pão com ovo / 5,00 ")
 