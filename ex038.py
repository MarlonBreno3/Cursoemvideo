numero = int(input('\033[1;34mDigite o primeiro valor:'))
numero1 = int(input('\033[1;35mDigite o segundo valor:'))
if numero > numero1:
    print('\033[1;34mO primeiro valor, {} é o maior.'.format(numero))
elif numero1 > numero:
    print('\033[1;35mO segundo valor, {} é o maior.'.format(numero1))
else:
    print('\033[1;32mNão existe valor maior, os dois são iguais.')
