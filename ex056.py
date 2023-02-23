acumidade = 0
maioridad = 0
cont = 0
nomevelho = ''
for c in range(1, 5):
    print('{} {}° pessoa{} '.format('=' * 20, c, '=' * 20))
    nome = str(input('Digite o nome da {}° pessoa:'.format(c))).strip()
    idade = int(input('Digite a idade:'))
    print("[ 1 ] Masculino [ 2 ] Feminino.")
    sexo = int(input("digite o sexo dessa pessoa:"))
    acumidade += idade
    if sexo == 2 and idade <= 20:
        cont = cont + 1
        print(cont)
    if c == 1 and sexo == 1:
        maioridad = idade
        nomevelho = nome
    if idade > maioridad and sexo == 1:
        maioridad = idade
        nomevelho = nome
print('Media de idade do grupo {:.1f} anos.'.format(acumidade / 4))
print('O homen mais velho tem {} e se chama {}. '.format(maioridad, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cont))
