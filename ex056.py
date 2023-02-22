acumidade = 0
maioridad = 0
cont = 0
for c in range(1, 5):
    print('{} {}° pessoa{} '.format('=' * 20, c, '=' * 20))
    nome = str(input('Digite o nome da {}° pessoa:'.format(c)))
    idade = int(input('Digite a idade:'))
    print("[ 1 ] Masculino [ 2 ] Feminino.")
    sexo = int(input("digite o sexo dessa pessoa:"))
    acumidade += idade
    if sexo == 2 and idade <= 20:
        cont =cont + 1
        print(cont)

    if c == 1 and sexo == 1:
        maioridad = idade
    else:
        if maioridad < idade and sexo == 1:
            maioridad = idade
print('Media de idade do grupo {:.0f} anos.'.format(acumidade / 4))
print('Idade do homen mais velho {} anos'.format(maioridad))
print('Mulheres com menos de vinte anos {}'.format(cont))
