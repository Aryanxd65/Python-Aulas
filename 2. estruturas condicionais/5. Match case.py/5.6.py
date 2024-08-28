import os
os.system("cls || clear")

print("""
1  -JANEIO 
2  - FEVEREIRO
3  - MARÇO   
4  - ABRIL
5  - MAIO 
6  - JUNHO 
7  - JULHO
8  - AGOSTO
9  - SETEMBRO
10 - OUTUBRO
11 - NOVEMBRO
12 - DEZEMBRO                                                               
      """)

mes = int(input("Digite um número de 1 a 12 pra escolher um mês do ano: "))

match(dia):
    case 1:
        print("JANEIRO ")
    case 2:
        print("FEVEREIRO ")
    case 3:
        print("MARÇO ")
    case 4:
        print("ABRIL ")
    case 5:
        print("MAIO")
    case 6:
        print("JUNHO")
    case 7:
        print("JULHO")   
    case 8:
        print("AGOSTO ")
    case 9:
        print("SETEMBRO ")
    case 10:
        print("OUTUBRO ")
    case 11:
        print("NOVEMBRO ")
    case 12:
        print("DEZEMBRO")
    case _:    
        print("INVALIDO")     