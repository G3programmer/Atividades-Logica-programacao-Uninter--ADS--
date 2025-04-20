#Vai ter que ser função para escolher def
total = 0  # Para fazer contagem geral do usuário
    
    # Parte que vai fazer a primeira função
def escolha_servico():    
    while True:  # repete até o usuário digitar corretamente
        try:
            print("  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  ")
            print("--|      MENU DE SERVIÇOS       |--")
            print("--|serviços do Gabriel Morozini |--")
            print("  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  ")
            print("--| 1) Digitalização            |--")
            print("--| 2) Impressão colorida       |--")
            print("--| 3) Impressão Preto e Branco |--")
            print("--| 4) Fotocópia                |--")
            print("  #-----------------------------#  ")
            
            escolha = int(input("Digite o número do serviço que deseja:\n$_"))
            if escolha == 1:
                return 1.10
            elif escolha == 2:
                return 1.00
            elif escolha == 3:
                return 0.40
            elif escolha == 4:
                return 0.20
            else:
                print("Opção inválida. Escolha um número entre 1 e 4.\n")
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.\n")

#Terminou a função de serviço e começa a quantia de páginas
def num_pagina():
    while True: 
        try:
            print("#~~~~~~~~~~~~~~~~~#-------------#~~~~~~~~~~~~~~~~#")
            print("|     Páginas     |             |    Descontos   |")
            print("#~~~~~~~~~~~~~~~~~#-------------#~~~~~~~~~~~~~~~~#")
            print("| Menos que 20......................|sem desconto|")
            print("| Menos que 200 e mais que 20.......|     15%    |")
            print("| Menos que 2000 e mais que 200.....|     20%    |")
            print("| Menos que 20000 e mais que 2000...|     25%    |")
            print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
            
            pag = int(input("Digite o número de página:\n$_"))
            
            if  pag>=20000:
               print("Excedeu o máximo de folhas!")
               continue
            elif pag>=2000:
                print("Você receberá 25% de desconto")
                return pag * 0.75
            elif pag>=200:
                print("Você receberá 20% de desconto")
                return pag * 0.80
            elif pag>=20:
                print("Você receberá 15% de desconto")
                return pag * 0.85
            elif pag > 0:
                print("Você não receberá desconto")
                return pag
            else:
                print("Deve ser um valor existente para as folhas!")
        except ValueError:
         print("Digite um valor válido para as folhas!")
        
         #Terceira função agora
def extra():
    while True:
        try:
            print("#~~~~~~~~~~~~~~~~~#")
            print("|  Serviço extra  |")
            print("#~~~~~~~~~~~~~~~~~#")
            print("| 1) Capa Simples |")
            print("| 2) Capa Dura    |")
            print("| 3) Finalizar    |")
            print("#~~~~~~~~~~~~~~~~~#")
            add = int(input("Digite o valor de uma opção se desejar:\n$_"))
            if add == 1:
             return 15.00
            elif add == 2:
             return 40.00
            elif add == 3:
             return 0
            else:
             print("Valor inválido, tente novamente!")
        except ValueError:
         print("Digite apenas números!")
        
        
    #Parte do main(principal)
try:
    escolha = escolha_servico() # Utilizando o valor da primeira função
    pag = num_pagina()          # Utilizando o valor da segunda função
    add = extra()              # Utilizando o valor da terceira função

    total = (escolha * pag) + add  # Cálculo do total final

    print(f"Total a pagar: R$ {total:.2f}")  # Apresenta ao usuário o total a pagar

except Exception as e:
    print("Ocorreu um erro inesperado. Por favor, tente novamente.")  # Se caso der algo errado
