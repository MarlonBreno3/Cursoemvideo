from random import randint
from time import sleep
cores = {'amarelo': '\033[33m', 'verde': '\033[32m', 'azul': '\033[34m', 'vermelho': '\033[31m'}
print('\033[1;33;44m-=-' * 10, '\033[m')
print('\033[1;33;44mGAME JOKENPO                   \033[m')
print('\033[1;33;44m-=-' * 10, '\033[m')
print('{}Escolha entre:'.format(cores['amarelo']))
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
escolha = int(input('Digite aqui sua escolha:'))
sleep(1.5)
print('{}JO'.format(cores['verde']))
sleep(1.5)
print('{}KEN'.format(cores['azul']))
sleep(1.5)
print('{}PO'.format(cores['vermelho']))
sleep(1.5)
aleatorio = randint(1, 3)
if aleatorio == 1 and escolha == 1:
    print('{}PEDRA Vs PEDRA'.format(cores['amarelo']))
    sleep(1.5)
    print('{}EMPATE'.format(cores['amarelo']))
elif aleatorio == 1 and escolha == 2:
    print('{}PEDRA Vs PAPEL'.format(cores['amarelo']))
    sleep(1.5)
    print('{}PARABÉNS, VOCÊ CONSEGUIU ME VENCER'.format(cores['verde']))
elif aleatorio == 1 and escolha == 3:
    print('{}PEDRA Vs TESOURA'.format(cores['amarelo']))
    sleep(1.5)
    print('{}VOCÊ PERDEU!!'.format(cores['vermelho']))
elif aleatorio == 2 and escolha == 1:
    print('{}PAPEL Vs PEDRA'.format(cores['amarelo']))
    sleep(1.5)
    print('{}VOCÊ PERDEU!!'.format(cores['vermelho']))
elif aleatorio == 2 and escolha == 2:
    print('{}PAPEL Vs PAPEL'.format(cores['amarelo']))
    sleep(1.5)
    print('{}EMPATE'.format(cores['azul']))
elif aleatorio == 2 and escolha == 3:
    print('{}PAPEL Vs TESOURA'.format(cores['amarelo']))
    sleep(1.5)
    print('{}PARABÉNS, VOCÊ CONSEGUIU ME VENCER'.format(cores['verde']))
elif aleatorio == 3 and escolha == 1:
    print('{}TESOURA Vs PEDRA'.format(cores['amarelo']))
    sleep(1.5)
    print('{}PARABÉNS, VOCÊ CONSEGUIU ME VENCER'.format(cores['verde']))
elif aleatorio == 3 and escolha == 2:
    print('{}TESOURA Vs PAPEL'.format(cores['amarelo']))
    sleep(1.5)
    print('{}VOCÊ PERDEU!!'.format(cores['vermelho']))
elif aleatorio == 3 and escolha == 3:
    print('{}TESOURA Vs TESOURA'.format(cores['amarelo']))
    sleep(1.5)
    print('{}EMPATE'.format(cores['azul']))
else:
    print('{}OCORREU UM ERRO, TENTE NOVAMENTE.'.format(cores['vermelho']))
