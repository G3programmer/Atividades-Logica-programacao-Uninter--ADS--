''' Deve cadastrar livro, buscar e remover
Deve cadastrar livro com ID, autor e editora
Pode buscar por ID ou autor
remove por ID '''

contador_id = 0
livros = []

class Livro:
    def __init__(self, ID, nome, autor, editora):
        self.ID = ID
        self.nome = nome
        self.autor = autor
        self.editora = editora

    def __str__(self):
        return f"ID: {self.ID} | Nome: {self.nome} | Autor: {self.autor} | Editora: {self.editora}"

def add_livro():
    global contador_id
    print("="*30)
    print("---| CADASTRO DE LIVRO |---")
    print("="*30)
    ID = str(contador_id)
    contador_id += 1
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do(a) autor(a) do livro: ")
    editora = input("Digite o nome da editora: ")
    novo_livro = Livro(ID, nome, autor, editora)
    livros.append(novo_livro)
    print("Livro cadastrado com sucesso!\n")

def search():
    print("="*23)
    print("---| BUSCAR LIVRO |---")
    print("="*23)
    print("  --------- MENU DE BUSCA ---------   ")
    print("#"+"-"*38+"#")
    print(" "*7+"| 1) Buscar todos os livros |")
    print(" "*7+"| 2) Buscar por ID          |")
    print(" "*7+"| 3) Buscar por Autor       |")
    print("#"+"-"*38+"#")

    opcao = input("Escolha uma opção de busca:\n>> ")

# Opção 1
    if opcao == '1':
        if not livros:
            print("Nenhum livro encontrado ou cadastrado.")
        else:
            print("\nLista de Livros:")
            for livro in livros:
                print(livro)
# Opção 2
    elif opcao == '2':
        busca_id = input("Digite o ID do livro:\n>> ")
        for livro in livros:
            if livro.ID == busca_id:
                print(livro)
                return
        print("Livro com esse ID não encontrado.")
    
# Opção 3    
    elif opcao == '3':
        busca_autor = input("Digite o nome do autor:\n>> ")
        encontrados = [livro for livro in livros if livro.autor.lower() == busca_autor.lower()]
        if encontrados:
            for livro in encontrados:
                print(livro)
        else:
            print("Nenhum livro encontrado para esse autor.")
    else:
        print("Opção inválida. Tente novamente.")


def remove():
    print("="*23)
    print("---| REMOVER LIVRO |---")
    print("="*23)
    remover = input("Digite o ID do livro que gostaria de remover:\n>>")
    for livro in livros:
        if livro.ID == remover:
            confirm = input("Tem certeza disso? (S/N):\n>>")
            if confirm.lower() == 's':
                livros.remove(livro)
                print("Livro removido com sucesso!")
                return
    print("Livro não encontrado")

# Menu principal
while True:
    print(" ="*20)
    print(" = = Biblioteca Do Gabriel Morozini =  = ")
    print(" ="*20)
    print("  --------- MENU PRINCIPAL ---------   ")
    print("#"+"-"*38+"#")
    print(" "*7+"| 1) Adicionar Livro |")
    print(" "*7+"| 2) Buscar Livro    |")
    print(" "*7+"| 3) Remover Livro   |")
    print(" "*7+"| 4) Sair            |")
    print("#"+"-"*38+"#")
    opt = int(input("Digite o número para uma função:\n>>"))

    if opt == 1:
        add_livro()
    elif opt == 2:
        search()
    elif opt == 3:
        remove()
    elif opt == 4:
        print("Obrigado por vir, até logo!")
        print('''
         @@@@@@@@@@@@@@@@@@@@@@              @@@@@@@@@@@@@@@@@@@@@@@        
        @@@               @@@@@@@@@@@@@@@@@@@@@@@@@               @@        
   @@@@@@@@                          @@                           @@@@@@@   
   @@   @@@                          @@                           @@   @@   
   @@   @@@                          @@                           @@   @@   
   @@   @@@  @@@@@@@@@@@@@@@@@@@@@   @@    @@@@@@@@@@@@@@@@@@@@   @@   @@   
   @@   @@@                   @@@@@  @@  @@@@@@                   @@   @@   
   @@   @@@                          @@                           @@   @@   
   @@   @@@   @@@@@@@@@@             @@             @@@@@@@@@@    @@   @@   
   @@   @@@  @@@@@@@@@@@@@@@@@@@@@@  @@  @@@@@@@@@@@@@@@@@@@@@@   @@   @@   
   @@   @@@                      @@  @@   @                       @@   @@   
   @@   @@@                          @@                           @@   @@   
   @@   @@@  @@@@@@@@@@@@@@@@@       @@       @@@@@@@@@@@@@@@@@   @@   @@   
   @@   @@@   @        @@@@@@@@@@@@  @@  @@@@@@@@@@@@@       @    @@   @@   
   @@   @@@                          @@                           @@   @@   
   @@   @@@                          @@                           @@   @@   
   @@   @@@  @@@@@@@@@@@@@@@@@@@     @@     @@@@@@@@@@@@@@@@@@@   @@   @@   
   @@   @@@                @@@@@@@@  @@  @@@@@@@@                 @@   @@   
   @@   @@@                          @@                           @@   @@   
   @@   @@@                          @@                           @@   @@   
   @@   @@@  @@@@@@@@@@@@@@@@@@@@@   @@   @@@@@@@@@@@@@@@@@@@@@   @@   @@   
   @@   @@@                    @@@@  @@  @@@@                     @@   @@   
   @@   @@@                          @@                           @@   @@   
   @@   @@@                          @@                           @@   @@   
   @@   @@@                          @@                           @@   @@   
   @@   @@@                          @@                           @@   @@   
   @@    @@@@@@@@@@@@@@@@@@@@@@@@@@@ @@  @@@@@@@@@@@@@@@@@@@@@@@@@@    @@   
   @@                            @@@@@@@@@@@                           @@   
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
        ''') 
        break
    else:
        print("Valor inválido, tente novamente!")
        continue
