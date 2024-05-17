import time

# Solicita ao usuário inserir o tempo inicial da contagem regressiva
tempo_inicial = int(input("Digite o tempo inicial da contagem regressiva em segundos: "))

# Inicializa o contador
tempo_restante = tempo_inicial

# Contagem regressiva
print("Contagem regressiva iniciada:")
while tempo_restante > 0:
    print(tempo_restante)
    tempo_restante -= 1
    time.sleep(1)  # Atraso de 1 segundo entre cada contagem

# Exibe a mensagem de explosão
print("Bomba explodiu!!! Boooooom")