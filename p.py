 # login
usuarioADM = [
["wallisson", "wallisson123@gmail.com", "#agronegócio"], ["guilherme", "guigui@gmail.com", "@algoritmos"], 
["renê", "gadelha@gmail.com", "coordenadoria26"], ["gilvan", "reigil@gmail.com", "gilvanII"]
]

usuarioCLI = [
["gabriel", "gabrielbastos@gmail.com", "zecabode"], ["zacarias", "zacarias01@gmail.com", "fazendajatobar###"]
]

usuarios = [usuarioADM, usuarioCLI]

animais = ["Bovinos", "Ovinos", "Caprinos", "Aves", "Equinos", "Suinos"]
produtos = []
# qualquer coisa a gente add mais listas
id_produto = 1

#contador de produtos !
login_do_usuario = 0
perfil_do_login = 0

while True:
    print("------ Bem vindo ao Agro app ------")
    print("1 - login do usuario" )
    print("2 - cadastro de usuario")
    print("3 - Sair")
    op = int(input(""))
    if op == 1:
        while True:
            email = input("Email: ").strip()
            if "@" not in email:
                print("Email inválido!")
            elif "gmail.com" not in email and "hotmail.com" not in email:
                print("Email inválido!")
            elif email[0] == "@":
                print("Email inválido!")
            elif email[-9:] != "gmail.com" and email[-11:] != "hotmail.com":
                print("Email inválido!")
            else:
                break
        
        while True:
            senha = input("Senha: ").strip()
            if len(senha) >= 8:
                break
            else:
                print("Senha inválida! Mínimo 8 caracteres.")

        encontrado = False

        
        for usuario in usuarioADM:
            if usuarioADM[1] == email and usuarioADM[2] == senha:
                print(f"Bem-vindo ADM {usuario[0]}!")
                encontrado = True
                while True: 
                    print("------ Bem vindo ao Terminal ------")
                    print("1 - Gerenciar Rebanho" )
                    print("2 - Gerenciar Produção e Derivados")
                    print("0 - Sair")
                    op = int(input(""))
                    if op == 0:
                        break
                    

        for usuario in usuarioCLI:
            if usuarioCLI[1] == email and usuarioCLI[2] == senha:
                print(f"Bem-vindo Cliente {usuario[0]}!")
                encontrado = True
                while True:
                    print("------ Bem vindo ao Terminal ------")
                    print("1 -  Efetuar compra" )
                    print("2 - Agendar Retirada/Transporte")
                    print("0 - Sair")
                    op = int(input(""))
                    if op == 0:
                        break
        
        for usuario in usuarioADM:
                    if usuario[1] != email and usuario[2] != senha:
                        print("Login ou senha incorretos.")

        for usuario in usuarioCLI:
                    if usuario[1] != email and usuario[2] != senha:
                        print("Login ou senha incorretos.")

    elif op == 2:
        while True:
            nome = input("Nome: ").strip()

            tem_numero = False
            i = 0

            while i < len(nome):

                if nome[i] >= "0" and nome[i] <= "9":
                    tem_numero = True

                i += 1

            if tem_numero:
                print("Inválido! O nome só pode ter letras.")

            else:
                break
        while True:
            email = input("Email: ").strip()
            if "@" not in email:
                print("Email inválido!")
            elif "gmail.com" not in email and "hotmail.com" not in email:
                print("Email inválido!")
            elif email[0] == "@":
                print("Email inválido!")
            elif email[-9:] != "gmail.com" and email[-11:] != "hotmail.com":
                print("Email inválido!")
            else:
                break
        
        while True:
            senha = input("Senha: ").strip()
            if len(senha) >= 8:
                break
            else:
                print("Senha inválida! Mínimo 8 caracteres.")
        while True:
            perfil = input("Perfil (adm/cliente): ").strip().lower()

            if perfil == "adm":
                usuarioADM.append([nome, email, senha])
                print("Usuário cadastrado com sucesso.")
                break  

            elif perfil == "cliente":
                usuarioCLI.append([nome, email, senha])
                print("Usuário cadastrado com sucesso.")
                break 

            else:
                print("Inválido! Tente novamente.")

    elif op == 3:
        print("Saindo...")
        print("volte sempre!")
        break
    else:
        print("Comando Inválido, tente novamente.")

# cliente
# admin

alteraranimais = input("Digite o nome do animal ! ")
novoanimal = input("Digite o nome do Novo animal ! ")
for posicao in range(len(animais)):
    if animais[posicao] == alteraranimais:
        animais[posicao] == novoanimal
        print(animais)

produtos = []

adicionarprodutos = input("Digite o nome do produto ! ")
alterarprodutos = input("Digite o nome do produto que vc deseja alterar ! ")
for posicao in range(len(animais)):
    if produtos[posicao] == adicionarprodutos:
        produtos[posicao] == alterarprodutos
        print(produtos)

produtos(len(produtos))
print(produtos)

# elif op == 4 :
#     print ("-" *  50)
#     nomedeanimal = input("Digite o nome do seu animal ! ")
#     for a in animais:
#         if a[0] == animais:
#             print("a[0], " | "a[1], " |" a[2], ")
animais.append([])
