print('-=-' * 13)
print('DETECTOR DE PALÍNDROMO')
print('-=-' * 13)
frase = str(input('Digite uma frase:')).strip().replace(' ', '').upper()
frase1 = frase[::-1]
print('O inverso de {} é {}'.format(frase, frase1))
if frase == frase1:
    print('A frase é um PALÍNDROMO!')
else:
    print('A frase NÃO é um PALÍNDROMO.')
