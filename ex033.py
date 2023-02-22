print('~~' * 30)
print('DIGITE TRÊS NÚMEROS')
print('~~' * 30)
verde = '\033[0:32m'
vermelho = '\033[0:31m'
primeiro = int(input('Digite o primeiro número:'))
segundo = int(input('Digite o segundo número:'))
terceiro = int(input('Digite o terceiro número:'))
print(verde)
if primeiro > segundo and primeiro > terceiro:
    print('O primeiro número é o maior entre os três.')
if segundo > primeiro and segundo > terceiro:
    print('O segundo número é o maior entre os três.')
if terceiro > segundo and terceiro > primeiro:
    print('O terceiro número é o maior entre os três.')
else:
    print('\033[0;34mO valores são iguais')
print(vermelho)
if primeiro < segundo and primeiro < terceiro:
    print('O primeiro número é o menor entre os três.')
if segundo < primeiro and segundo < terceiro:
    print('O segundo número é o menor entre os três.')
if terceiro < primeiro and terceiro < segundo:
    print('O terceiro número é o menor entre os três.')
else:
    print('')
