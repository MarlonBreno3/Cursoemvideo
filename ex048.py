s = 0
v = 0
dividido = 0
n = 0
for c in range(1, 501, 2):
    dividido = c % 3
    if dividido == 0:
        v += 1
        s += c
print('A soma de todos os {} valores solicitados é {} '.format(v, s))
