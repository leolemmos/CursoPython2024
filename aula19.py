#AULA 19 - ATIVIDADE PRÁTICA

# Imprime o cabeçalho do programa
print("*********************  DESCONTO DE INSS *********************")

# Solicita ao usuário o valor do salário
salario = float(input("Digite o seu salário: R$ "))

# Calcula o desconto do INSS com base no salário
if salario <= 2500:
    aliquota = 7.5
    desconto = salario * (aliquota / 100)
elif salario <= 5500:
    aliquota = 9
    desconto = salario * (aliquota / 100)
elif salario <= 10000:
    aliquota = 12
    desconto = salario * (aliquota / 100)
elif salario <= 20000:
    aliquota = 14
    desconto = salario * (aliquota / 100)
else:
    aliquota = 0
    desconto = 0

# Calcula o salário líquido
salario_liquido = salario - desconto

# Exibe o valores
print("\nValor do salário: R$", salario)
print("Alíquota de INSS aplicada:", aliquota, "%")
print("Valor do desconto de INSS: R$", desconto)
print("Valor líquido a receber: R$", salario_liquido)