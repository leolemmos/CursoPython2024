#AULA 21 - PROJETO DE SISTEMA DE LOGIN DE ACESSO (ajustando..)

# Função para realizar o login de acesso
def fazer_login(usuarios_cadastrados):
    print("\n************ LOGIN DE ACESSO ************")
    login = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")
    if login == "admin" and senha == "admin":
        print("Acesso Liberado!")
        return True
    elif login in usuarios_cadastrados and usuarios_cadastrados[login] == senha:
        print("Acesso Liberado!")
        return True
    else:
        print("Acesso Negado!")
        return False

# Função para criar cadastro e fazer login
def criar_cadastro(usuarios_cadastrados):
    print("\n************ CRIAR CADASTRO ************")
    novo_login = input("Digite o novo login: ")
    nova_senha = input("Digite a nova senha: ")
    usuarios_cadastrados[novo_login] = nova_senha
    print("Cadastro criado com sucesso!")
    # Automaticamente faz login com as novas credenciais
    print("\nAcessando o sistema com o novo cadastro:")
    fazer_login(usuarios_cadastrados)

# Imprime o cabeçalho do sistema de acesso
print("******************** SISTEMA DE ACESSO ********************")

# Dicionário para armazenar usuários cadastrados e suas senhas
usuarios_cadastrados = {}

# Loop principal do programa
while True:
    print("\nOpções:")
    print("Digite [01] Para fazer login de acesso")
    print("Digite [02] Para Criar seu cadastro")
    print("Digite [03] Para sair do Sistema")

    opcao = input("Digite a opção desejada: ")

    if opcao == "01":
        fazer_login(usuarios_cadastrados)
    elif opcao == "02":
        criar_cadastro(usuarios_cadastrados)
    elif opcao == "03":
        print("Muito Obrigado pelo acesso, até mais..")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")