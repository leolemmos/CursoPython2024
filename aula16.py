#AULA 16 - ATIVIDADE PRÁTICA - ESTRUTURA DE DECISÃO

# Solicita as quantidades dos produtos
quantidade_produto_A = int(input("Digite a quantidade do Produto A: "))
quantidade_produto_B = int(input("Digite a quantidade do Produto B: "))
quantidade_produto_C = int(input("Digite a quantidade do Produto C: "))
quantidade_produto_D = int(input("Digite a quantidade do Produto D: "))
quantidade_produto_E = int(input("Digite a quantidade do Produto E: "))

# Soma as quantidades dos produtos
total_estoque = (quantidade_produto_A + quantidade_produto_B + 
                 quantidade_produto_C + quantidade_produto_D + 
                 quantidade_produto_E)

# Exibe as quantidades dos produtos e o total do estoque
print("\nQuantidade do Produto A:", quantidade_produto_A)
print("Quantidade do Produto B:", quantidade_produto_B)
print("Quantidade do Produto C:", quantidade_produto_C)
print("Quantidade do Produto D:", quantidade_produto_D)
print("Quantidade do Produto E:", quantidade_produto_E)
print("Total do estoque:", total_estoque)

# Verifica se o estoque está baixo ou normal
if total_estoque < 100:
    print("Situação do Estoque: Estoque Baixo")
else:
    print("Situação do Estoque: Estoque Normal")