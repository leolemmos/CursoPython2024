import time

# Texto a ser digitado
target_text = "asdfg " * 10  # 10 repetições de "asdfg "

# Função para calcular a precisão
def calculate_accuracy(input_text, target_text):
    correct_chars = 0
    for input_char, target_char in zip(input_text, target_text):
        if input_char == target_char:
            correct_chars += 1
    return (correct_chars / len(target_text)) * 100

# Função principal do programa de treinamento de digitação
def typing_test():
    print("Digite o seguinte texto exatamente como está:")
    
    # Exibe o texto em colunas
    
    for _ in range(10):
        print("asdfg", end=" ")
    print("\n")
    
    print("Pressione Enter quando estiver pronto para começar...")
    input()  # Espera o usuário pressionar Enter

    start_time = time.time()  # Inicia a contagem do tempo
    user_input = input("\nComece a digitar: ")  # Captura a digitação do usuário
    end_time = time.time()  # Termina a contagem do tempo

    elapsed_time = end_time - start_time  # Calcula o tempo decorrido
    accuracy = calculate_accuracy(user_input, target_text)  # Calcula a precisão

    # Verifica se o usuário passou no teste
    if accuracy >= 70 and elapsed_time <= 120:
        result = "Aprovado"
    else:
        result = "Reprovado"

    # Exibe os resultados
    print("\nResultado do Teste de Digitação:")
    print(f"Precisão: {accuracy:.2f}%")
    print(f"Tempo: {elapsed_time:.2f} segundos")
    print(result)

# Executa o programa de treinamento de digitação
if __name__ == "__main__":
    typing_test()