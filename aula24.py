
def cumprimentar():   #FUNÇÃO 01
    print("Bom dia")
    
def cumprimentar2(): #FUNÇÃO 02   
    print("Bom tarde!")

def main(): # FUNÇÃO PRINCIPAL
    
    cumprimentar()  # Chama o método cumprimentar
    cumprimentar2()    

if __name__ == "__main__":
    main()
    
"""
 * Ponto de entrada do programa
 * Isso é útil para definir um comportamento padrão ou um ponto de entrada para um script.
 * if __name__ == "__main__":: Garante que main seja executado apenas quando o script for
   executado diretamente
 * __name__ é uma variável especial que contém o nome do módulo que está sendo executado.
 * main(): Função principal do programa que chama a função
"""