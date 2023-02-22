print('{:=^40}'.format('LOJAS GUANABARA'))
preço = float(input('Digite o valor do produto:'))
print('Condição de pagamento: R$')
print('[1] Á vista dinheiro / cheque: 10% de desconto.')
print('[2] Á vista no cartão: 5% de desconto.')
print('[3] Em até 2× no cartão: preço normal.')
print('[4] 3× ou mais no cartão: 20% de juros.')
pagamento = int(input('Digite aqui a forma de pagamento:'))
if pagamento == 1:
    conta = (preço-(preço * 0.10))
    print('O produto que custava R${:.2f}, com 10% de desconto passará a custar R${:.2f}.'.format(preço, conta))
elif pagamento == 2:
    conta = (preço - (preço * (5/100)))
    print('O produto que custava R${:.2f}, com 5% de desconto passára a custar R${:.2f}.'.format(preço, conta))
elif pagamento == 3:
    conta = preço / 2
    print('O produto pacelado em 2 parcelas fica R${:.2f} cada'.format(conta))
elif pagamento == 4:
    parcelas = int(input('Em quantas parcelas deseja dividir ?'))
    juros = (preço + (preço * 0.20))
    conta = juros / parcelas
    print("Seu produto será parcelado em {}× de R${} COM JUROS\n"
          "Sua compra de R${} vai custar {} no final.".format(parcelas, conta, preço, juros))
else:
    print('\033[1;31mHOUVE UM ERRO TENTE NOVAMENTE')
