print('~~' * 15)
print('\033[0;34mANALISANDO NÚMERO PAR OU IMPAR\033[m')
print('~~' * 15)
numero = int(input('Digite um número inteiro:'))
par = (numero % 2)
if par == 0:
    print('O número {} é \033[1;35mPAR\033[m.'.format(numero))
else:
    print('O número {} é \033[1;35mIMPAR\033[m.'.format(numero))
