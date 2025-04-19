total = 0  # Para fazer contagem geral do usuário

while True:
    print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ")
    print("--|      MENU DE SERVIÇOS       |--")
    print("--|serviços do Gabriel Morozini |--")
    print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
    print("--| 1) Digitalização            |--")
    print("--| 2) Impressão colorida       |--")
    print("--| 3) Impressão Preto e Branco |--")
    print("--| 4) Fotocópia                |--")
    print("  -------------------------------  ")

    Opcoes = int(input("Escolha uma opção de serviço:\n$_ "))

    if Opcoes == 1:
        num = int(input("Digite o número de páginas a ser digitalizada:\n$_> "))

        if num < 20:
            print("Sem desconto")
            valor = num * 1.10
        elif num >= 20 and num < 200:
            print("Desconto de 15%")
            valor = num * 1.10 * 0.85
        elif num >= 200 and num < 2000:
            print("Desconto de 20%")
            valor = num * 1.10 * 0.80
        elif num >= 2000 and num < 20000:
            print("Desconto de 25%")
            valor = num * 1.10 * 0.75
        else:
            print("Máximo de páginas ultrapassado")
            continue

        total += valor

    elif Opcoes == 2:
        print("Você escolheu Impressão colorida.")
        num = int(input("Quantas páginas deseja imprimir?\n$_> "))
        valor = num * 1.50  # exemplo de valor
        total += valor

    elif Opcoes == 3:
        print("Você escolheu Impressão Preto e Branco.")
        num = int(input("Quantas páginas deseja imprimir?\n$_> "))
        valor = num * 0.80  # exemplo de valor
        total += valor

    elif Opcoes == 4:
        print("Você escolheu Fotocópia.")
        num = int(input("Quantas cópias deseja fazer?\n$_> "))
        valor = num * 0.60  # exemplo de valor
        total += valor

    else:
        print("Opção inválida, tente novamente!")
        continue

    cont = input(f"\nO valor parcial é R${total:.2f}. Deseja mais algum serviço? (S/N): ").upper()
    if cont != 'S' and cont !='s':
        print(f"\nValor total a pagar: R${total:.2f}")
        print("Obrigado por usar nossos serviços!")
        break
