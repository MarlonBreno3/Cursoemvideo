print('_'*30)
print('Carros alugados')
print('_'*30)
km = float(input('Digite a quantidade de km percorridos: '))
dia = int(input('Quantidade de dias alugado(s):'))
km1 = (km * 0.15)
dia1 = (dia * 60)
print('valor cobrado pelo km percoridos:R${:.2f}'.format(km1))
print('Valor cobrado por dia(s) alugados:R${:.2f}'.format(dia1))
print('\033[1;32mTotal R${:.2f}'.format(km1 + dia1))
