#AULA 17 - ATIVIDADE PRÁTICA

# Imprime o cabeçalho do programa de doação
print("PROGRAMA DE DOAÇÃO")

# Imprime as opções de doação
print("Opções para doar:")
print("Digite [01] Para Doar R$ 10,00")
print("Digite [02] Para Doar R$ 20,00")
print("Digite [03] Para Doar R$ 30,00")
print("Digite [04] Para Doar R$ 40,00")
print("Digite [05] Para Doar R$ 50,00")

# Solicita ao usuário a opção de doação
opcao_doacao = input("Digite o número da opção desejada: ")

# Verifica a opção de doação e exibe a mensagem correspondente
if opcao_doacao == "01":
    print("Você escolheu doar R$ 10,00. Obrigado pela sua doação!")
elif opcao_doacao == "02":
    print("Você escolheu doar R$ 20,00. Obrigado pela sua doação!")
elif opcao_doacao == "03":
    print("Você escolheu doar R$ 30,00. Obrigado pela sua doação!")
elif opcao_doacao == "04":
    print("Você escolheu doar R$ 40,00. Obrigado pela sua doação!")
elif opcao_doacao == "05":
    print("Você escolheu doar R$ 50,00. Obrigado pela sua doação!")
else:
    print("Opção inválida! Por favor, escolha uma opção válida de 01 a 05.")