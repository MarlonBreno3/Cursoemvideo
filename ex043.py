print('-=-' * 10)
print('CALCULO IMC')
print('-=-' * 10)
peso = float(input('Digite seu peso:(Kg)'))
altura = float(input('Digite a sua altura:(M)'))
imc = peso / ((altura ** 2))
if imc < 18.5:
    print('Seu imc {:.1f}, Você está ABAIXO DO PESO.'.format(imc))
elif 18.5 <= imc <= 25:
    print('Seu imc {:.1f},Você está com o PESO IDEAL.'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu imc {:.1f}, você está com SOBREPESO.'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu imc {:.1f}, você está com OBESIDADE'.format(imc))
elif imc > 40:
    print('Seu imc {:.1f}, Você está com OBESIDADE MÓRBIDA.'.format(imc))
