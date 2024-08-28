import os
os.system("cls || clear")

login_salvo = "fabio"
senha_salva = 555

for i in range(3):
    while True:
        login = str(input("Digite seu login: "))
        senha = int(input("Digite sua senha: "))
        if login == login_salvo and senha == senha_salva :
            print("Bem-vindo")
            break    
        else:
            print("Login ou senha inválidos.")    
            
        
