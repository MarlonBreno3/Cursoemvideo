import random
print('~'*30)
print('ORDEM DE APRESENTAÇÃO')
print('~'*30)
aluno1 = str(input('Digite o nome do primeiro aluno:'))
aluno2 = str(input('Digite o nome do segundo aluno:'))
aluno3 = str(input('Digite o nome do terceiro aluno:'))
aluno4 = str(input('Digite o nome do quarto aluno:'))
sorteio = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(sorteio)
print('\033[1;34mOrdem de apresentação {}.'.format(sorteio))
