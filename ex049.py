print('-=-' * 10)
print('\033[1;32mTABUADA\033[m')
print('-=-' * 10)
numero = int(input('Digite o número da tabuada que deseja:'))
multip = 0
for c in range(0, 10):
    multip += 1
    print('{} × {} = {}'.format(numero, multip, multip * numero))
