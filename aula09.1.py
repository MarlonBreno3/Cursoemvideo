frase = 'Curso em Vídeo Python'
print(frase.lower().find('vídeo'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.capitalize())
print(frase.title())
print('-'.join(frase))
print('-'.join(frase.split()))
dividido = frase.split()
print(dividido[2])
print(dividido[2][3])
print(frase.startswith('mundo'))
print(frase.endswith('Python'))
dividido1 = frase.rsplit(sep=None, maxsplit= 1)
print(dividido1[1])
