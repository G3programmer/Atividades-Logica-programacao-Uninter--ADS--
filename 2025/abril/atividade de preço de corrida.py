km = float(input('Digite o valor percorrido: '))
dias = int(input('Quantos dias foi utilizados? '))

preco = (dias*60) + (0.15 * km)

print(f'Km = {km}. Dias = {dias}.')
print(f' Valor a pagar: {preco}')
