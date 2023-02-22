from emoji import emojize
from time import sleep
print('-=-' * 17)
print('CONTAGEM REGRESSIVA PARA A QUEIMA DE FOGOS DE ARTIFÍCIO')
print('-=-' * 17)
start = int(input('Digite o número 1 para começar:'))
if start == 1:
    for c in range(10, 1-1, -1):
        print(c)
        sleep(1)
    for n in range(0, 15):
        print(emojize(":fogos_de_artifício:", language="pt")*50)
        sleep(0.25)
else:
    print('\033[1;31mCONTAGEM REGRESSIVA CANCELADA')
