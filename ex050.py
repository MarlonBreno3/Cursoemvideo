soma = 0
for c in range(0, 6):
    numero = int(input('Digite um valor:'))
    divisão = numero % 2
    if divisão == 0:
        soma += numero
print('Soma de todos os números pares {}.'.format(soma))
