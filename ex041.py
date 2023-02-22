from datetime import date
print('-=-' * 10)
print('CATEGORIA DO ATLETA')
print('-=-' * 10)
nascimento = int(input('Digite o seu ano de nascimento:'))
anoatual = date.today().year
idade = anoatual - nascimento
if idade >=0 and idade <= 9:
    print('Você tem {} anos sua classificação é \033[34mMIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos sua classificação é \033[34mINFANTIL.'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos sua classificação é \033[34mJUNIOR'.format(idade))
elif idade > 19 and idade <= 20:
    print('Você tem {} anos sua classificação é \033[34mSÊNIOR'.format(idade))
elif idade > 20 and idade < 115:
    print('Você tem {} anos sua classificação é \033[34mMASTER.'.format(idade))
elif idade < 0 or idade >= 115:
    print('\033[31mOcorreu um erro com a sua idade, tente novamente.')
else:
    print('\033[31mOcorreu um erro tente novamente.')

