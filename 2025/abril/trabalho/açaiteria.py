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
    print("| 3) Terminar |")
    print("---------------")

    prod = int(input("Digite o número do seu pedido: "))

#Aqui é a subopção de tamanho depois de escolher o que o usuário deseja
    if prod == 1:
        print("\nBoa escolha! Mas qual tamanho você gostaria?")
        print("----------------------")
        print("| 1)   Pequeno (P)   |")
        print("| 2)     Médio (M)   |")
        print("| 3)    Grande (G)   |")
        print("| 4)     Voltar      |")
        print("----------------------")


# Se caso o usuário escolher errado, poderá voltar com a opção 4, se não, pode continuar e se for inválido retornará ao início

        tamanho = int(input("Digite o número do tamanho do seu pedido: "))

        if tamanho in [1, 2, 3]:
            quant = int(input("Perfeito! Agora digite a quantidade que você gostaria de pedir: "))
            precos = {1: 11.00, 2: 16.00, 3: 20.00}
            
            #Aqui ele calculará o preço conforme o tamanho e a quantidade
            subtotal = precos[tamanho] * quant
            total += subtotal
        elif tamanho == 4:
            continue
        else:
            print("Valor inválido. Tente novamente.")
            continue

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
            
            #Aqui ele calculará o preço conforme o tamanho e a quantidade
            subtotal = precos[tamanho] * quant
            total += subtotal
        elif tamanho == 4:
            continue
        else:
            print("\nValor inválido. Tente novamente.\n")
            continue

    elif prod == 3:
        break

    else:
        print("Essa opção não existe! Por favor, tente novamente\n\n\n")
        continue

    # Aqui ele da a opção de pedir mais coisa se preferir, para concluir deverá negar e para pedir mais deverá aceitar
    continuar = input(f"\nGostaria de mais alguma coisa? (S/N)\nTotal até agora: R${total:.2f}\n").strip().upper()
    if continuar == "N":
        break

# Saiu do While ele agradecerá e mostrará o valor a pagar
print(f"\n===== Pedido Finalizado =====\nTotal a pagar: R${total:.2f}\nObrigado pela preferência!\n")
print("""
 ------------------:: . @@@@@@ ..::-------------------------- 
 -----------------:-. @%*=+   #@..-:------------------------- 
 -----------------:: @=-=+==-.. @.::------------------------- 
 -----------------:. @-=--===-- .%.:------------------------- 
 ------------:::::: :+==----+=-..@ :------------------------- 
 -------::.         @+-===--==-:% .:------------------------- 
 ---:::.  .=@@@@@@@@@@+--=+++++*@ -:------------------------- 
 --:-.  *@%+---====--=+@@+=:-#%@  :::::::::::::::------------ 
 --.  @@#+++++++====++-..=@@@@                  .:----------- 
 :. +@*+==+****+++++=++==:. @    @@@%#@@@@%@@@@@    ::------- 
 ..@%+=++++=. -:::-===+++=-..@@@@%#. @@   .   :%%#@   .:----- 
  -#+=++=+=-.+@@@@+----++===. @: ...-   .----:.. @@@%:  ::--- 
 .@+==+===+.==-::.-=@@-==+=-=.=@.-=:  ..  .--=--.  +@*@. .::- 
 .%========++==-----  .@@==*:. #.=:.%@@@@@..==:.     **%@ .-: 
 -%+++==++===-----==+=:  #@+++#@:+-@@     @::.-%@@@+. -*#@  : 
 :%=++=+++::-...:--====-...#*#*  .-: @ *@  @.=@    *@: ++*@ . 
 .@==+===:.-+@@%=---=+===-. %+=%@@*-@@@@-  @.+ #@@   @:=+=#.  
  #*=++=+=-+-:..:@@-:-+=-== +%.  .%+.@@*@ @*.+ @@@@  -#=+=+@  
 . @*==+=+======:  =@-=+*-..@=@@@@++... .=@.--.@-@@  #+-=+=%. 
 :. @%*=++++===*+=-  *+:-+#@=::..::-.:.@%:..--..%  =@@%#=++%= 
 :-.. @%*===+++++**=. @@@*-======-.@.... .--===:=@*#+-.-=++#= 
 -::-.. @@%#==-==+-++=@=-===+=+===.@@ %*+=-:.... ..@+@#==+=%: 
 --::::.   +@@@%%%@@@@:-**+=++=+==: @@  .@@@@@#+%@@*::-=+++@  
 -------::.           @ :*#+=+==+==.+@@@      *@.::-==++++% . 
 -----------:::::::::.:@..+#++=+++=:.*:@@@@@@@@..=++====+%@ : 
 --------------------: #@ .=##++=+==-.@## @@@@@.==+=++++%@ .: 
 --------------------:. .@. .+#*=+=++:..@@@@@..:=++=*=*@= .-: 
 ---------------------::. %@. .=#*++===+......-=+=++#%@ ..::- 
 ----------------------::.. *@# ..*#++=--======+=*%@@ . ::--- 
 ------------------------::. . @@%=**++====+*%%@@@.   ::----- 
 --------------------------:::.  . *@@@@@@@@@*..   ::-------- 
""")
