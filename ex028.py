from random import randint
from time import sleep
print('~~' * 32)
print('TENTE ADIVINHAR O NUMÉRO PENSADO PELO COMPUTADOR.')
print('~~' * 32)
jogador = int(input('Digite um número de 0 a 5:'))
computador = randint(0, 5)
sleep(2)
print('O número pensado pelo computador foi {}.'.format(computador))
if computador == jogador:
    print('\033[1;32mPARABÉNS VOCÊ GANHOU!!!')
else:
    print('\033[1;31mVOCÊ PERDEU!!!')
