print("===== Seja Bem-vindo à Açaiteria do Gabriel Morozini! =====")  # Apenas a apresentação para o usuário
print("               ===== Tabela de Valores =====")
print("     ---| Tamanho |  Cupuaçu (CP)  |  Açaí (AC)  |---")
print("     ---|    P    |    R$ 9.00     |   R$ 11.00  |---")
print("     ---|    M    |   R$ 14.00     |   R$ 16.00  |---")
print("     ---|    G    |   R$ 18.00     |   R$ 20.00  |---")
print("     --------------------------------------------------\n")
print("     -------- Escolha o que gostaria de pedir! ------")
# Aqui eu decidi fazer escolha por numeração para ser intuitivo para a escolha do usuário
print("---------------")
print("| 1)   Açaí   |")
print("| 2)  Cupuaçu |")
print("---------------")

# Aqui o usuário digita a opção do menu anterior 
# e se for inválido ele deverá escolher novamente
prod = int(input("Digite o número do seu pedido: "))

# Se o usuário Digitar 1 ele escolherá Açaí
if prod == 1:
    print("\nBoa escolha! Mas qual tamanho você gostaria?")
    print("----------------------")
    print("| 1)   Pequeno (P)   |")
    print("| 2)    Médio  (M)   |")
    print("| 3)    Grande (G)   |")
    print("| 4)     Voltar      |")
    print("----------------------")
    tamanho = int(input("Digite o número do tamanho do seu pedido: "))

elif prod == 2:
    print("\nBoa escolha! Mas qual tamanho você gostaria?")
    print("----------------------")
    print("| 1)   Pequeno (P)   |")
    print("| 2)    Médio  (M)   |")
    print("| 3)    Grande (G)   |")
    print("| 4)     Voltar      |")
    print("----------------------")
    tamanho = int(input("Digite o número do tamanho do seu pedido: "))

else:
    print("Valor inválido, tente novamente!")
