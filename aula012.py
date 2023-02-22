nome = str(input('Qual é o seu nome?')).strip()
if nome.upper() == 'GUSTAVO':
    print('Que nome bonito!')
elif nome.upper() == 'PEDRO' or nome == 'MARIA' or nome == 'PAULO':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jessica juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))
