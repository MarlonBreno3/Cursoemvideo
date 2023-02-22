largura = float(input('Largura da parede em (m):'))
altura = float(input('Altura da parede em (m):'))
area = (altura * largura)
print('Para pintar uma parede de {} por {} é necessario {:.2f}l de tinta.'.format(altura, largura, area/2))
