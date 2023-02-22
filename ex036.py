print('-=-'*10)
print('\033[1;36mEMPRÉSTIMO BANCARIO\033[m')
print('-=-'*10)
salario = float(input('Qual o seu salario?R$'))
valorcasa = float(input('Digite o valor casa:R$'))
parcelas = float(input('Digite em quantos anos você deseja parcelar:'))
# calculo do valor pago por mês
prestaçaomensal = valorcasa / (parcelas * 12)
# calculo de 30% do salario
trintadosalario = salario * (30/100)
if prestaçaomensal > trintadosalario:
    print('\033[1;31mEmpréstimo negado!')
else:
    print('\033[1;32mEmprestimo aprovado!')
    print('\033[1;36mValor da casa R${} valor das parcela mensais R${:.2f}'.format(valorcasa, prestaçaomensal))

