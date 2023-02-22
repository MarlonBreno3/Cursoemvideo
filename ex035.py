print('CONDIÇÃO DE FORMAÇÃO DE TRIÂNGULOS')
reta1 = float(input('Comprimento da primeira reta:'))
reta2 = float(input('Segunda reta:'))
reta3 = float(input('Terceira reta:'))
# Verificando o primeiro menor número
if reta1 + reta2 > reta3 and reta3 + reta2 > reta1 and reta3 + reta1 > reta2:
    print('\033[1;32mÉ possivel que exista um triângulo com essas medidas')
else:
    print('\033[1;31mNão é possivel formar um triângulo com essas medidas')
# acompanhar correção
