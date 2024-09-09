import os
os.system("cls || clear")

num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))


def soma(a,b):
    return a+b

def subtraçao(a,b):
    return a-b

def multiplicação(a,b):
    return a*b

def divisão(a,b):
    if b == 0:
        return
    return a/b

print("Soma:", soma(num1, num2))
print("Subtração:", subtraçao(num1, num2))
print("Soma:", multiplicação(num1, num2))
print("Soma:", divisão(num1, num2))






