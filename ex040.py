print('Média Escolar')
nota = float(input('Digite a primeira nota:'))
nota1 = float(input('Digite a seguda nota:'))
media = (nota + nota1) / 2
if media < 5.0:
    print('Sua média foi de {:.1f}  você está \033[1;31mREPROVADO\033[m'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua média foi de {:.1f} você está de \033[1;34mRECUPERAÇÃO\033[m.'.format(media))
elif media >= 7.0:
    print('Sua média foi de {:.1f} você foi \033[1;32mAPROVADO\033[m.'.format(media))