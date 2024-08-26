import os
os.system("cls || clear")


primeiro_numero = int(input("Digite aqui o primeiro numero: "))
segundo_numero = int(input("Digite aqui o segundo numero: "))

opcao = input("Digite uma opçao (+ - * / ): ")

match(opcao):
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero
    case _:
        print("Opção inválida")

print(f"Reseultado: {resultado}")
print("===FIM===")
    