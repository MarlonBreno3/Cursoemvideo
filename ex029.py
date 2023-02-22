velocidade = float(input('Digite a velocidade do carro:'))
if velocidade > 80.0:
    multa = (velocidade - 80) * 7
    print("\033[1;31mVOCÊ EXCEDEU O LIMITE DE VELOCIDADE DE 80KM/H E "
          "DEVE PAGAR UMA DE MULTA DE R${:.2f}.".format(multa))
else:
    print('\033[1;32mBoa viagem!!')
