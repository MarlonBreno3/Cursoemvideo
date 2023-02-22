n1 = input('Digite algo:')
print(
    "É númerico: {}\nÉ alfabético: {}\nÉ espaço: {}\nÉ minúsculo:{}\nÉ maiusculo:{}\nQual o tipo primitivo:{}\nÉ alfanúmerico:{} "
    .format(n1.isnumeric(), n1.isalpha(), n1.isspace(), n1.islower(), n1.isupper(), type(n1),n1.isalnum()))
