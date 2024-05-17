#AULA 15 - ESTRUTURA DE DECISÃO

#PROGRAMA CALCULANDO IDADE

# Solicita o ano atual e o ano de nascimento
ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Calcula a idade da pessoa
idade = ano_atual - ano_nascimento

# Exibe a idade da pessoa
print("\nIdade:", idade)

# Verifica se a pessoa é maior ou menor de idade
if idade >= 18:
    print("Situação: Maior de idade")
else:
    print("Situação: Menor de idade")