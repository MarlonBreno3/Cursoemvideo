from random import randint
from time import sleep
itens = ['PEDRA', 'PAPEL', 'TESOURA']
computador = randint(0, 2)
print('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada?'))
sleep(1)
print('JO')
print('-=-' * 10)
print('Escolha do computador {} :'.format(itens[computador]))
print('Escolha do jogador {} :'.format(itens[jogador]))
print('-=-' * 10)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU!!!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!!!')
    else:
        print('JOGADA INVÁLIDA.')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!!!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVALIDA!!!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU!!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
