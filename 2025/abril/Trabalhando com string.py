frase = input('Digite uma frase: ')
tam = len(frase)  #len para pegar o tamanho da string

frase2 = frase[:int(tam/2)]

print(frase2[-2:]) # Apresentará as 2 ultimas letras da frase
