print('-=-' * 10)
print('ANALISE DE TRIÂNGULOS')
print('-=-' * 10)
lado1 = float(input('Digite o tamanho do primeiro lado:'))
lado2 = float(input('Segundo lado:'))
lado3 = float(input('Terceiro lado:'))
if lado1 == lado2 == lado3:
    classificação = ('\033[1;32mEQUILÁTERO')
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    classificação = ('\033[1;33mESCALENO')
else:
    classificação = ('\033[1;34mISÓSCELES')
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('Com essas medidas é possivel formar um triângulo {}.'.format(classificação))
else:
    print('\033[1;31mNão é possível formar um triângulo com essas medidas.')
