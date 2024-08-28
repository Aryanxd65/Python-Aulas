import os
os. system("cls || clean")

contador = 0

login_salvo = "fabio"
senha_salva = "555"

while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    contador += 1
        
    if login == login_salvo and senha == senha_salva :
        print("Bem-vindo")
        break    
    else:
        print("Login ou senha inválidos.")    
        print(f"Tentativa: {contador} \n")
        if contador == 3:
            break          
print("===FIM===")            

         