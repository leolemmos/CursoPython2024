#AULA 18 - ATIVIDADE PRÁTICA

# Imprime o cabeçalho do programa
print("CALCULADORA DE IMC")

# Solicita ao usuário o peso em quilogramas
peso = float(input("Digite o seu peso em quilogramas: "))

# Solicita ao usuário a altura em metros
altura = float(input("Digite a sua altura em metros: "))

# Calcula o IMC (Índice de Massa Corporal)
imc = peso / (altura ** 2)

# Exibe o peso e altura digitados
print("\nPeso:", peso, "kg")
print("Altura:", altura, "m")

# Exibe o resultado do IMC e a classificação de acordo com a tabela
print("Seu IMC é:", imc)

# Verifica a classificação do IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
elif imc < 35:
    print("Classificação: Obesidade grau I")
elif imc < 40:
    print("Classificação: Obesidade grau II")
else:
    print("Classificação: Obesidade grau III (mórbida)")