print('--'*10)
print ('ALUGUEl DE CARROS')
print('--'*10)
km = float(input('Qual a distancia percorrida em KM:'))
dia = int (input('Dias alugados:'))
print ('Valor a se pagar pelos dias alugados R${:.2f} .'.format(dia * 60))
print ('A valor a ser pagar por KM percorridos:R${:.2f}'.format(km * 0.15))
print ('\033[1;32mtotal R${:.2f}'.format((dia * 60) + (km * 0.15)))