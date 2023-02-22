import math
angulo = float(input('Digite um ângulo qualquer:'))
# print('O ângulo {}:'.format(angulo))
print('O ângulo {} tem o SENO {:.2f}.'.format(angulo, math.sin(math.radians(angulo))))
print('O ângulo {} tem o COSSENO {:.2f}'.format(angulo, math.cos(math.radians(angulo))))
print('O ângulo {} tem o TANGENTE {:.2}'.format(angulo, math.tan(math.radians(angulo))))
