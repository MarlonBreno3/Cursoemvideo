from datetime import datetime
print('ANALISE DE ANO BISSEXTO')
ano = int(input('Que ano quer analisar ? Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = (datetime.today().year)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} \033[1;32mÉ BISSEXTO.'.format(ano))
else:
    print('O ano {} \033[0;31mNÃO é BISSEXTO'.format(ano))
