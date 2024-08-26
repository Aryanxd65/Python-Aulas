import os
os.system("cls || clear")

print("""
1 - Domingo
2 - Segunda
3 - Terça   
4 - Quarta
5 - Quinta
6 - Sexta 
7 - Sabado                                  
      """)

dia = int(input("Digite um numero de 1 a 7 pra escolher o dia da semana: "))

match(dia):
    case 1:
        print("Final de Semana ")
    case 2:
        print("Dia últil ")
    case 3:
        print("Dia últil ")
    case 5:
        print("Dia últil ")
    case 5:
        print("Dia últil")
    case 5:
        print("Dia últil")
    case 5:
        print("FIm de semana")
    case _:
        print("Invalido")     
