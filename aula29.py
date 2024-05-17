#AULA 29 - ESTRUTURA DE REPETIÇÃO WHILE -TABUADA

# Solicita ao usuário inserir o número para a tabuada
numero_tabuada = int(input("Digite o número para a tabuada: "))

# Inicializa o contador
valor = 1

# Exibe a tabuada de multiplicação usando um loop while
print(f"Tabuada de Multiplicação do {numero_tabuada}:")
while valor <= 10:
    resultado = numero_tabuada * valor
    print(f"{numero_tabuada} x {valor} = {resultado}")
    valor += 1
    
    