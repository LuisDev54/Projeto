usuarioADM = [
["wallisson", "wallisson123@gmail.com", "#agronegócio"], ["guilherme", "guigui@gmail.com", "@algoritmos"], 
["renê", "gadelha@gmail.com", "coordenadoria26"], ["gilvan", "reigil@gmail.com", "gilvanII"]
]

usuarioCLI = [
["gabriel", "gabrielbastos@gmail.com", "zecabode"], ["zacarias", "zacarias01@gmail.com", "fazendajatobar###"]
]

usuarios = [usuarioADM, usuarioCLI]
usuario_gilvan_animais = [" Bovinos", "Ovinos", "Caprinos", "Aves", "Suinos"]
animais = [
    ["bovino", "azul", "AB12", "disponível para venda"]
]

Produtos = [
    ["Leite", 100, 4.00]
    ["Milho", 500, 1.80],
    ["Feijão", 200, 6.50],
    ["Arroz", 350, 4.20],
    ["Soja", 800, 2.90],
    ["Café", 150, 15.00],
    ["Cana-de-açúcar", 1200, 0.75],
    ["Algodão", 400, 5.40],
    ["Mandioca", 450, 2.10],
    ["Tomate", 280, 3.80],
    ["Batata", 350, 2.70]
]

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
            if usuario[1] == email and usuario[2] == senha:
                print(f"Bem-vindo ADM {usuario[0]}!")
                encontrado = True
                while True: 
                    print("------ Bem vindo ao Terminal ------")
                    print("1 - Gerenciar Rebanho" )
                    print("2 - Gerenciar Produção e Derivados")
                    print("0 - Sair")
                    op = int(input(""))
                    if op == 1:
                        while True:
                            print("-" * 10)
                            print("1 - Cadastrar animal" )
                            print("2 - Buscar Animal")
                            print("3 - Atualizar animal")
                            print("4 - remover animal")
                            print("0 - sair")
                            print("-" * 10)
                            op = int(input(""))
                            if op == 1:
                               
                                while True:

                                    print("Tipos disponíveis:")
                                    print("Bovino, Suino, Ave, Ovino, Caprino")
                                    print("-" * 10)
                                    tipo = input("Digite o tipo: ").lower()

                                    if tipo != "bovino" and tipo != "suino" and tipo != "ave" and tipo != "ovino" and tipo != "caprino":
                                        print("Tipo inválido! Tente novamente.")
                                    else:
                                        break
                                
                                
                                while True:
                                    print("Escolha uma cor de brinco para o animal abaixo.")
                                    print("As cores disponíveis são azul, amarelo e verde.")
                                    print("-" * 10)
                                    brinco = input("")
                                    if brinco == "azul" or brinco == "amarelo" or brinco == "verde":
                                        print("-" * 10)
                                        break
                                    else:
                                        print("Digite uma cor válida!")
                                
                                while True:
                                    identificacao = input("Digite a identificação: ")
                                    valido = True
                                    
                                    for letra in identificacao:
                                        if "A" <= letra <= "Z":
                                            valido = True
                                        elif "a" <= letra <= "z":
                                            valido = True
                                        elif "0" <= letra <= "9":
                                            valido = True
                                        else:
                                            valido = False
                                    
                                    for animal in animais:
                                        if animal[0] == tipo:
                                            if animal[1] == brinco:
                                                if animal[2] == identificacao:
                                                    print("Erro! Já existe um animal com esse brinco.")
                                                    valido = False
                                    
                                    if len(identificacao) != 4:
                                        print("Erro! A identificação deve ter 4 caracteres.")
                                        valido = False
                                    

                                    if valido == True:
                                            break
                                

                                while True:
                                    
                                    print("\nStatus disponíveis:")
                                    print("1 - Em lactação")
                                    print("2 - Para engorda")
                                    print("3 - Disponível para venda")

                                    status = int(input("Digite o status: "))

                                    if status == 1:
                                        status = "em lactação"
                                        break
                                    elif status == 2:
                                        status = "para engorda"
                                        break
                                    elif status == 3:
                                        status = "disponível para venda"
                                        break
                                    else:
                                        print("Erro! Status inválido.")
                                
                                animal = [tipo, brinco, identificacao, status]
                                animais.append(animal)
                                print("Animal cadastrado com sucesso!")
                            
                            if op == 2:
                                tipo = input("Digite o tipo do animal: ").lower()
                                brinco = input("Digite a cor do brinco: ").lower()
                                identificacao = input("Digite a identificação: ")

                                encontrado = False

                                for animal in animais:

                                    if animal[0] == tipo:
                                        if animal[1] == brinco:
                                            if animal[2] == identificacao:

                                                print("\nAnimal encontrado!")
                                                print("Tipo:", animal[0])
                                                print("Cor do brinco:", animal[1])
                                                print("Identificação:", animal[2])
                                                print("Status:", animal[3])

                                                encontrado = True

                                if encontrado == False:
                                    print("Animal não encontrado.")

                            elif op == 3:
                                while True:
                                    tipo = input("Digite o tipo do animal: ").lower()
                                    brinco = input("Digite a cor do brinco: ").lower()
                                    identificacao = input("Digite a identificação: ")

                                    encontrado = False

                                    for animal in animais:
                                        if animal[0] == tipo:
                                            if animal[1] == brinco:
                                                if animal[2] == identificacao:

                                                    encontrado = True
                            
                                    if encontrado == False:
                                        print("Animal não encontrado.")
                                    else:
                                        print("\nAnimal encontrado!")
                                        break
                                while True:

                                    print("\nStatus disponíveis:")
                                    print("1 - Em lactação")
                                    print("2 - Para engorda")
                                    print("3 - Disponível para venda")

                                    status = int(input("Digite o novo status: "))

                                    if status == 1:
                                        animal[3] = "em lactação"
                                        break

                                    elif status == 2:
                                        animal[3] = "para engorda"
                                        break

                                    elif status == 3:
                                        animal[3] = "disponível para venda"
                                        break

                                    else:
                                        print("Erro! Status inválido.")

                                print("Animal atualizado com sucesso!")
                                break
                            
                            elif op == 4:

                                tipo = input("Digite o tipo do animal: ").lower()
                                brinco = input("Digite a cor do brinco: ").lower()
                                identificacao = input("Digite a identificação: ")

                                encontrado = False

                                for i in range(len(animais)):

                                    if animais[i][0] == tipo:

                                        if animais[i][1] == brinco:

                                            if animais[i][2] == identificacao:

                                                animais.pop(i)

                                                print("Animal removido com sucesso!")

                                                encontrado = True

                                                break

                                if encontrado == False:
                                    print("Animal não encontrado.")
                            
                            elif op == 0:
                                break   
                            else:
                                print("Comando Inválido, tente novamente.")
                    
                    elif op == 2:
                        while True:
                            print("\n=== GERENCIAR PRODUÇÃO E DERIVADOS ===")
                            print("1 - Registrar leite ordenhado")
                            print("2 - Cadastrar produto")
                            print("3 - Atualizar produto")
                            print("4 - Remover produto")
                            print("0 - Sair")
                            op = int(input("Escolha uma opção: "))
                            if op == 1:

                                litros = float(input("Digite a quantidade de litros ordenhados: "))

                                Produtos.append(["Leite", litros, 4])

                                print("Produção registrada com sucesso!")

        
                            elif op == 2:
                                nome_produto = input("Nome do produto: ").strip()

                                peso = float(input("Peso do produto (kg): "))

                                valor = float(input("Valor de venda: R$ "))

                                produto = [nome_produto, peso, valor]

                                Produtos.append(produto)

                                print("Produto adicionado ao estoque!")

        
                                derivados = False
                            elif op == 3:
                                print("\n=== PRODUÇÃO DE LEITE ===")
                                for leite in Produtos:
                                    print(leite, "litros")
                                    if (leite >=  8, "litros"):
                                        print("Voce tem estoque de leite suficiente para pronduzir queijo !")
                                        print("\n=== PRODUTOS FABRICADOS ===")

                                for produto in derivados:

                                    print("Produto:", produto[0])
                                    print("Peso:", produto[1], "kg")
                                    print("Valor: R$", produto[2])

                            elif op == 4:
                                break

                            else:
                                print("Opção inválida!")
        
                                
                    if op == 0:
                        break
                    else:
                        print("Comando Inválido, tente novamente.")

        for usuario in usuarioCLI:
            if usuario[1] == email and usuario[2] == senha:
                print(f"Bem-vindo Cliente {usuario[0]}!")
                encontrado = True
                while True:
                    print("* - 10 Bem vindo ao Terminal * - 10 ")
                    print("1 -  Efetuar compra" )
                    print("2 - Agendar Retirada/Transporte")
                    print("0 - Sair")
                    op = int(input(""))
                    if op == 1:
                        print("")
                    if op == 2:
                        print("test")
                    if op == 0:
                        break
                    else:
                        print("Comando Inválido, tente novamente.")
        
        if encontrado == False:
            print("Login ou senha incorretos.")

    elif op == 2:

        while True:

            nome = input("Nome: ").strip()

            tem_numero = False
            invalido = False
            i = 0

            while i < len(nome):
                if nome[i] >= "0" and nome[i] <= "9":
                    tem_numero = True
                elif nome[i] != " " and not ("A" <= nome[i] <= "Z") and not ("a" <= nome[i] <= "z"):
                    invalido = True
                i += 1

            if tem_numero == True or invalido == True:
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
        print("Volte sempre!")
        break
    else:
        print("Comando Inválido, tente novamente !")

# cliente
# admin
 # 1
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
    