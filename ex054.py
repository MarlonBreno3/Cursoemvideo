from datetime import datetime
print('GRUPO DA MAIORIDADE')
anoatual = datetime.today().year
cont = 0
for c in range(1, 8):
    nascimeto = int(input('Ano de nascimeto da {}° pessoa:'.format(c)))
    calculo = (anoatual - nascimeto)
    if calculo >= 18:
        cont += 1
print('Das 7 pessoas {} são maiores de idade.'.format(cont))
