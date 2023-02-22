
print('-=-' * 15)
print('NUMEROS PRIMOS')
print('-=-' * 15)
cont = 0
cont1 = 0
numero = int(input('Digite um número inteiro:'))
for c in range(1, numero + 1):
    resto = numero % c
    if resto != 0:
        cont1 += 1
        print('\033[31m{}'.format(c), end=' ')
    elif resto == 0:
        cont += 1
        print('\033[33m{}'.format(c), end=' ')
if cont == 2:
    print('\nO número {} É PRIMO.'.format(numero))
else:
    print('\nO número {} NÃO É UM NÚMERO PRIMO, pois ele foi dividido {} vezes.'.format(numero, cont1))
