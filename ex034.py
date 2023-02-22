print('~~'*20)
print('CALCULO DE AUMENTO DE SALARIO')
print('~~'*20)
salario = float(input('qual o seu salario?R$'))
if salario > 1250:
    aumento = (salario * 0.10) + salario
    porcentagem = '10%'
else:
    aumento = (salario * 0.15) + salario
    porcentagem = '15%'
print('\033[0;32mO seu salario terá um aumento percentual de {} '
      'e passará a valer R${:.2f} agora.'.format(porcentagem, aumento))
