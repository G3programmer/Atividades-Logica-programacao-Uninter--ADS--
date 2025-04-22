''' Deve cadastrar livro, buscar e remover
Deve cadastrar livro com ID, autor e editora
Pode buscar por ID ou autor
remove por ID '''

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
    #Método para adicionar livro (com ID, autor e editora)
    class Livro:
        def __init__(self, ID, autor, editora):
            self.
