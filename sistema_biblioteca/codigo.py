# Programa de Gestão de Livros
# Este programa permite ao usuário cadastrar livros, listar todos os livros cadastrados 
# e sair do sistema. O sistema mantém uma lista de livros, onde cada livro é armazenado
# com seu título, autor e ano de publicação. O usuário interage com o sistema através de 
# um menu de opções, podendo escolher entre cadastrar um novo livro, listar os livros já 
# cadastrados ou sair do programa.

livros = []

# Função para cadastrar um novo livro
def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de publicação do livro: ")

    # Adiciona o livro na lista
    livros.append({"titulo": titulo, "autor": autor, "ano": ano})
    print(f"Livro '{titulo}' cadastrado com sucesso!\n")

# Função para listar os livros cadastrados
def listar_livros():
    if len(livros) == 0:
        print("Não há livros cadastrados.\n")
    else:
        print("Livros cadastrados:")
        for livro in livros:
            print(f"Título: {livro['titulo']} | Autor: {livro['autor']} | Ano: {livro['ano']}")
        print()

# Menu principal
while True:
    print("Sistema de Gestão de Livros")
    print("1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção (1, 2 ou 3): ")
    
    if opcao == "1":
        cadastrar_livro()
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        print("Saindo do sistema... Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.\n")