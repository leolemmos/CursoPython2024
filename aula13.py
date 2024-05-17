#AULA 13 - ATIVIDADE PRÁTICA

#Crie um boletim escolar com cadastro de nome, notas e resolver média das notas

nome = "0"
nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
nota4 = 0.0

print(" **************** BOLETIM ESCOLAR *****************")
nome = input("Digite o nome do aluno(a): ")
nota1 = float(input("Digite a nota 01 : "))
nota2 = float(input("Digite a nota 02 : "))
nota3 = float(input("Digite a nota 03 : "))
nota4 = float(input("Digite a nota 04 : "))

media = (nota1 + nota2 + nota3 + nota4)/4

print(" ------------------- RESULTADO --------------------")
print("Nome: ", nome)
print("Nota 01: ", nota1)
print("Nota 02: ", nota2)
print("Nota 03: ", nota3)
print("Nota 04: ", nota4)
print("Nota Média: ", media)