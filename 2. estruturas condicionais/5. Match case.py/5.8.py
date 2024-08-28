import os
os. system("cls || clear")
print("solicitar preço do produto")

desconto = 0
preco_final = 0
preco_parcelado = 0

preco_produto = int(input("Digite o valor do produto: "))

print("Se for a vista digite 1")
print("Se for a prazo digite 2")

opcao = int(input("Digite a opção 1 ou 2: "))

match (opcao):
    case 1:
        desconto = preco_produto * 0.10
        preco_final = preco_produto - desconto

        print(f"Preço do produto:R$ {preco_produto}")
        print("Forma de pagamento : A vista")
        print(f"Valor do desconto: {desconto} ")
        print(f"Total a pagar: {preco_final}")
    case 2:
        print("Digite um numero de parcelas ( ate 6x ) ")
        parcelas = int(input("Digite o numero de parcelas: "))
        preco_parcelado = preco_produto / parcelas   
        preco_final = preco_parcelado

        print(f"Valor do produto : {preco_produto}")
        print("Forma de Pagamento :Á prazo ")
        print(f"Quantidade de parcelas: {parcelas}")
        print(f"Total á prazo: {preco_final}")
    case _:
        print("Não é valido")    
