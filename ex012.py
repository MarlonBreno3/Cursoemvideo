preco = float(input('Digite o valor do produto:R$'))
desconto = (preco-(preco*0.05))
print('Aplicando o desconto de 5% o produto que custava R${:.2f} fica R${:.2f};'.format(preco, desconto))
