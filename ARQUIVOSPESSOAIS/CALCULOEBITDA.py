print('~~'*25)
print('TAXA DE CRECIMENTO ANUAL COMPOSTA (CAGR)')
print('Período de análise 5 anos')
EBITDA1 = float(input('Digite o EBITDA do 1° ano:'))
EBITDA2 = float(input('Digite o EBITDA do 5° ano:'))
calculo = (((EBITDA2 / EBITDA1)**(1 / 5) - 1) * 100)
print('A taxa de crescimento anual dessa empressa é de {:.2f}%'.format(calculo))
