print('-=-' * 15)
print('PROGRESSÃO ARITMÉTICA')
print('-=-' * 15)
primeirotermo = int(input('Digite o primeiro termo:'))
razao = int(input('DIGITE O RAZÃO:'))
for c in range(primeirotermo, primeirotermo + (razao * 10), razao):
    print(c, end=' → ')
print('ACABOU')
