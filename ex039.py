from datetime import date
print('\033[1;30;42mALISTAMENTO MILITAR')
nascimento = int(input('Informe seu ano de nascimento:'))
anoatual = date.today().year
idade = anoatual - nascimento
menor = 18 - idade
maior = anoatual - (nascimento + 18)
if idade < 18:
    print('FALTAM {} ano(s) para você se alistar'.format(menor))
elif idade == 18:
    print('JÁ ESTÁ NA HORA DE VOCÊ SE ALISTAR PROCURE UM QUARTEL MAIS PRÓXIMO!!!')
elif idade > 18:
    print('SEU ALISTAMENTO JÁ PASSOU, VOCÊ DEVERIA TER SE ALISTADO A {} ANO(s) ATRÁS.'.format(maior))
# falta fazer teste e adicionar mais cores
