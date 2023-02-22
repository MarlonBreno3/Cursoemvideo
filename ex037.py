print('-=-' * 10)
print('\033[1;36mBASE DE CONVERSÃO\033[m')
print('-=-' * 10)
numero = int(input('Digite o número que deseja converter:'))
print('Escolha a base de conversão:')
print('\033[1;32m[1] Binario')
print('\033[1;33m[2] Octal')
print('\033[1;34m[3] Hexadecimal\033[m')
base = int(input('Base de conversão:'))
if base == 1:
    print('Em decimal {} em \033[1;32mBINARIO {}.'.format(numero, bin(numero).replace('0b', '')))
elif base == 2:
    print('EM decimal {} em \033[1;33mOCTAL {}'.format(numero, oct(numero).replace('0o', '')))
elif base == 3:
    print('Em decimal {} em \033[1;34m HEXADECIMAL {}'.format(numero, hex(numero).replace('0x', '')))
    # terminar fazer testes e adicionar cores
