print('-=-'*15)
print('\033[1;33TODOS OS NÚMEROS PARES E ÍMPARES')
print('-=-' * 15)
escolha = int(input('Digite 1 para ver os numeros ímpares e 2 para os pares: '))
if escolha == 1:
    for c in range(1, 50, 2):
        print(c, end=' ')
    print('FIM')
if escolha == 2:
    for c in range(2, 52, 2):
        print(c, end=' ')
    print('FIM')
