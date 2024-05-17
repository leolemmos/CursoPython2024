import time

def contar_regressiva():
    tempo_restante = 15
    print("Bomba armada. Contagem regressiva iniciada...")
    while tempo_restante > 0:
        print(tempo_restante)
        tempo_restante -= 1
        time.sleep(1)  # Atraso de 1 segundo entre cada contagem
    print("Boooooooom!!!!!")

def jogo_desarme_bomba():
    print("******************* JOGO DESARME A BOMBA *****************")
    print("Escolha bem qual a cor do fio você deve cortar. Caso contrário, a bomba será armada em 30 segundos.")
    print("Opções:")
    print("Para cortar o fio amarelo, digite [01]")
    print("Para cortar o fio verde, digite [02]")
    print("Para cortar o fio azul, digite [03]")
    print("Para cortar o fio preto, digite [04]")

    escolha = input("Escolha uma opção: ")

    if escolha == "03":
        print("Parabéns! Você desativou a bomba.")
    else:
        contar_regressiva()

# Inicia o jogo
jogo_desarme_bomba()