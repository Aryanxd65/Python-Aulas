import os
os.system("cls || clear")

def imc (peso,altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
 if imc < 18.5:
    return "abaixo do peso"
 elif 18.5 <= imc <24.9:
    return "Peso Normal"
 elif 25 <= imc < 29.9:
    return "Sobrepeso"
 elif 30 <= imc < 34.9:
    return "Obesidade grau 1"
 elif 35 <= imc <39.9:
    return "Obesidade grau 2"
 else:
    return "Obesidade grau 3"
 
#entrada

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

#processamento
imc = calcular_imc(peso,altura)
classificacao = verificar_classificacao(imc)

#saída

 