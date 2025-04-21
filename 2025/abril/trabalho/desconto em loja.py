# Se o valor for menor que 2500, desconto de 0%
# Se valor igual ou mais que 2500 e menor que 6000, será de 4%
# Se igual ou mais que 6000 e menor q 10000 desconto de 7%
# Se igual ou mais q 10000 deve ser de 11%

print('=== Bem Vindo a loja do Gabriel Morozini ===')
unit = float(input('Insira o valor do seu produto:\n'))
quant = int(input('Digite a quantidade desse produto:\n'))

total = unit*quant

print(f'O valor sem desconto: R${total}')

# Se o valor for menor que 2500, desconto de 0%
if total < 2500:
    desconto = 0

# Se valor igual ou mais que 2500 e menor que 6000, será de 4%
elif total < 6000:
    desconto = 4

# Se igual ou mais que 6000 e menor q 10000 desconto de 7%
elif total < 10000:
    desconto = 7

# Se igual ou mais q 10000 deve ser de 11%
else:
    desconto=11
    
valor_desco = total * (desconto / 100)
result = total - valor_desco
print(f'O seu desconto foi de {desconto}%, logo o valor com desconto será de {result}\n')
print('Obrigado por comprar! Volte sempre! ;)') 
