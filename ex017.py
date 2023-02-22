from math import hypot
co = float(input('Qual o comprimento do cateto oposto:'))
ca = float(input('Qual o comprimemento do cateto adjacente:'))
print('Com as médidas dos catetos {} e {} o comprimento da hipotenusa é igual a {:.2f}. '.format(co, ca, hypot(co, ca)))
