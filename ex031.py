km = float(input('Digite a distância da viagem em KM:'))
if km <= 200:
    viagem = (km * 0.50)
    print('O preço da passagem vai custar R${:.2f}'.format(viagem))
else:
    viagem = (km * 0.45)
    print('O preço da passagem vai custar R${:.2f}'.format(viagem))
