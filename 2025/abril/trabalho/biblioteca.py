''' Deve cadastrar livro, buscar e remover
Deve cadastrar livro com ID, autor e editora
Pode buscar por ID ou autor
remove por ID '''

contador_id = 1

    #Método para adicionar livro (com ID, nome, autor e editora)
    class Livro:
        def __init__(self, ID, nome, autor, editora):
            self.ID = ID
            self.ID = nome
            self.autor = autor
            self.ID = editora
            
        def __str__(self):
              return f"ID: {self.ID} | Nome: {self.nome} | Autor: {self.autor} | Editora: {self.editora}"
livros=[]
        
#Parte para cadastrar
    def add_livro():
        print("="*23)
        print("---| CADASTRO DE LIVRO |---")
        print("="*23)
        # Para gerar um ID automático
        ID = str(contador_id) #ID será valor contador_id
        contador_id+=1 # Acrescenta +1 por ID
        nome = input("Digite o nome do livro: ")
        autor = input("Digite o nome do(a) autor(a) do livro: ")
        editora = input("Digite o nome da editora: ")
        novo_livro = livro(ID, nome, autor, editora) #Criando livro conforme os campos
        livros.append(novo_livro) #adicionado
        print("livro cadastrado com sucesso!\n")
#Principal
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
        searsh();
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
