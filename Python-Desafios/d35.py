n1 = int(input(f'Digite um número: '))
n2 = int(input(f'Digite um número: '))
n3 = int(input(f'Digite um número: '))


def validacao():
    print(f'\nNão forma nenhum triangulo, pois o maior valor é maior do que a soma dos dois menores!')


def formatriangulo():
    print(f'\nForma um triangulo!')


if (n1 > n2) and (n1 > n3):
    if n2+n3 > n1:
        formatriangulo()
    else:
        validacao()
elif (n2 > n1) and (n2 > n3):
    if n1+n3 > n2:
        formatriangulo()
    else:
        validacao()
elif (n3 > n1) and (n3 > n2):
    if n2+n1 > n3:
        formatriangulo()
    else:
        validacao()
else:
    print(f'\nO maior valor está duplicado em outra variável')
