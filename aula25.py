def mostrar_cardapio_pizzas():
    """Mostra o cardápio de pizzas."""
    pizzas = [
        ("Pizza Margherita", 25.00),
        ("Pizza Calabresa", 30.00),
        ("Pizza Quatro Queijos", 35.00),
        ("Pizza Portuguesa", 32.00),
        ("Pizza Frango com Catupiry", 28.00),
        ("Pizza Pepperoni", 40.00),
        ("Pizza Vegetariana", 27.00),
        ("Pizza de Chocolate", 33.00)
    ]
    print("\nCardápio de Pizzas:")
    for nome, preco in pizzas:
        print(f"{nome}: R$ {preco:.2f}")

def mostrar_cardapio_hamburgers():
    """Mostra o cardápio de hambúrgueres."""
    hamburgers = [
        ("Hambúrguer Clássico", 15.00),
        ("Cheeseburger", 17.00),
        ("Hambúrguer de Frango", 12.00),
        ("Hambúrguer Vegetariano", 18.00),
        ("Double Bacon Burger", 25.00),
        ("Hambúrguer com Ovo", 14.00),
        ("Hambúrguer Barbecue", 22.00),
        ("Hambúrguer Picante", 20.00)
    ]
    print("\nCardápio de Hambúrgueres:")
    for nome, preco in hamburgers:
        print(f"{nome}: R$ {preco:.2f}")

def mostrar_cardapio_bebidas():
    """Mostra o cardápio de bebidas."""
    bebidas = [
        ("Refrigerante", 8.00),
        ("Suco Natural", 10.00),
        ("Água Mineral", 5.00),
        ("Chá Gelado", 9.00),
        ("Cerveja", 12.00),
        ("Vinho", 25.00),
        ("Coquetel", 20.00),
        ("Café", 7.00)
    ]
    print("\nCardápio de Bebidas:")
    for nome, preco in bebidas:
        print(f"{nome}: R$ {preco:.2f}")

def mostrar_menu():
    """Mostra o menu principal e processa a escolha do usuário."""
    while True:
        print("\nDigite [ 01 ] Cardápio de Pizzas")
        print("Digite [ 02 ] Cardápio de Hambúrgueres")
        print("Digite [ 03 ] Cardápio de Bebidas")
        print("Digite [ 04 ] Sair do Sistema")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "01":
            mostrar_cardapio_pizzas()
        elif opcao == "02":
            mostrar_cardapio_hamburgers()
        elif opcao == "03":
            mostrar_cardapio_bebidas()
        elif opcao == "04":
            print("Obrigado pela preferência, volte sempre!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Executa o programa de cardápio
if __name__ == "__main__":
    mostrar_menu()