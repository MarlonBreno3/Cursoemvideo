maior = 0
menor = 0
for c in range(1, 6):
    peso = int(input('Digite o peso da {}° pessoa:'.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso digitado foi {}Kg.'.format(maior))
print('O menor peso digitado foi {}Kg.'.format(menor))
