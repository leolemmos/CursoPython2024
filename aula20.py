#AULA 20- ATIVIDADE PRÁTICA

# Imprime o cabeçalho do sistema de acesso
print("*************** SISTEMA DE ACESSO ***************")

# Solicita ao usuário o nome de usuário e senha
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

# Verifica se o nome de usuário e senha estão corretos
if usuario == "leonardo" and senha == "1234":
    print("Acesso Liberado!")
else:
    print("Acesso Negado!")