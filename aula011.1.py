print('\033[1;31;43mOlá, mundo!\033[m')
print('\033[4;97;45mOlá, mundo!\033[m')
print('\033[7;33;44mOlá mundo\033[m')
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[0;30;107m'}
nome = 'Marlon'
print('Olá! Muito prazer em te conhecer {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
