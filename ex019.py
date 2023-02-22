import random
from time import sleep
print('~'*47)
print('SORTEIO PARA ESCOLHER QUEM IRÁ APAGAR O QUADRO')
print('~'*47)
aluno1 = str(input('Nome do primeiro aluno:'))
aluno2 = str(input('Nome do segundo aluno:'))
aluno3 = str(input('Nome do terceiro aluno:'))
aluno4 = str(input('Nome do quarto aluno:'))
sort = (aluno1, aluno2, aluno3, aluno4)
print('...')
sleep('SORTEANDO... ')
print('\033[1;33mAluno sorteado para apagar o quadro foi {}!'.format(random.choice([aluno1, aluno2, aluno3, aluno4])))
