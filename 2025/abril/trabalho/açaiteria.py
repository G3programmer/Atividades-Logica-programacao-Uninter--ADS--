total = 0  # Para fazer contagem geral do usuário

while True:
    print("===== Seja Bem-vindo à Açaiteria do Gabriel Morozini! =====")  # Apenas a apresentação para o usuário
    print("               ===== Tabela de Valores =====")
    print("     ---| Tamanho |  Cupuaçu (CP)  |  Açaí (AC)  |---")
    print("     ---|    P    |    R$ 9.00     |   R$ 11.00  |---")
    print("     ---|    M    |   R$ 14.00     |   R$ 16.00  |---")
    print("     ---|    G    |   R$ 18.00     |   R$ 20.00  |---")
    print("     --------------------------------------------------\n")
    print("     -------- Escolha o que gostaria de pedir! ------")
    print("---------------")
    print("| 1)   Açaí   |")
    print("| 2)  Cupuaçu |")
    print("---------------")

    prod = int(input("Digite o número do seu pedido: "))

    if prod == 1:
        print("\nBoa escolha! Mas qual tamanho você gostaria?")
        print("----------------------")
        print("| 1)   Pequeno (P)   |")
        print("| 2)     Médio (M)   |")
        print("| 3)    Grande (G)   |")
        print("| 4)     Voltar      |")
        print("----------------------")

        tamanho = int(input("Digite o número do tamanho do seu pedido: "))

        if tamanho in [1, 2, 3]:
            quant = int(input("Perfeito! Agora digite a quantidade que você gostaria de pedir: "))
            precos = {1: 11.00, 2: 16.00, 3: 20.00}
            subtotal = precos[tamanho] * quant
            total += subtotal
        elif tamanho == 4:
            continue
        else:
            print("Valor inválido. Tente novamente.")

    elif prod == 2:
        print("\nBoa escolha! Mas qual tamanho você gostaria?")
        print("----------------------")
        print("| 1)   Pequeno (P)   |")
        print("| 2)     Médio (M)   |")
        print("| 3)    Grande (G)   |")
        print("| 4)     Voltar      |")
        print("----------------------")

        tamanho = int(input("Digite o número do tamanho do seu pedido: "))

        if tamanho in [1, 2, 3]:
            quant = int(input("Perfeito! Agora digite a quantidade que você gostaria de pedir:\n"))
            
            precos = {1: 9.00, 2: 14.00, 3: 18.00}
            
            subtotal = precos[tamanho] * quant
            
            total += subtotal
        elif tamanho == 4:
            continue
        else:
            print("Valor inválido. Tente novamente.")

     continuar = input(f"\nGostaria de mais alguma coisa? (S/N)\nTotal até agora: R${total:.2f}\n").strip().upper()
    if continuar == "N":
        break

# FORA DO WHILE: EXIBE TOTAL FINAL
print(f"\n===== Pedido Finalizado =====\nTotal a pagar: R${total:.2f}\nObrigado pela preferência!")
