#AULA 14 - ESTRUTURA DE DECISÃO

# Solicita o nome do aluno e as notas
nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibe o nome do aluno e suas notas
print("\nNome do aluno:", nome_aluno)
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Nota 4:", nota4)
print("Média:", media)

# Verifica se o aluno foi aprovado ou reprovado
if media >= 7.0:
    print("Situação: Aluno Aprovado")
else:
    print("Situação: Aluno Reprovado")