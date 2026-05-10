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
                print("Email inválido! # 1")
            elif email[0] == "@":
                print("Email inválido!")
            elif email[-9:] != "gmail.com" and email[-11:] != "hotmail.com":
                print("Email inválido! # 2")
            else:
                break
        
        while True:
            senha = input("Senha: ")
            if len(senha) >= 8:
                break
            else:
                print("Senha inválida! Mínimo 8 caracteres.")
        while True: 
            for e in usuarios:
                if [nome, email, senha] in usuarioADM:
                    print("test")
                    break
                elif [nome, email, senha] in usuarioCLI:
                    print("test")
                    break
                elif [nome, email, senha] not in usuarioCLI or usuarioADM:
                    print("usuário não encontrado.")
                    break #Break n ta funcionando 

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
                print("Email inválido! # 1")
            elif email[0] == "@":
                print("Email inválido!")
            elif email[-9:] != "gmail.com" and email[-11:] != "hotmail.com":
                print("Email inválido! # 2")
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
                usuarioADM.append([nome, email, senha]).lower()
                print("Usuário cadastrado com sucesso.")
                break  

            elif perfil == "cliente":
                usuarioCLI.append([nome, email, senha]).lower()
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
