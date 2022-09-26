n1 = int(input(f'Digite um número: '))
n2 = int(input(f'Digite um número: '))
n3 = int(input(f'Digite um número: '))
if (n1 > n2) and (n1 > n3):
    if n2+n3 > n1:
        print(f'Forma um triangulo!')
elif (n2 > n1) and (n2 > n3):
    if n1+n3 > n2:
        print(f'Forma um triangulo!')
elif (n3 > n1) and (n3 > n2):
    if n2+n1 > n3:
        print(f'Forma um triangulo!')
else:
    print(f'\nNão forma nenhum triangulo, pois o maior valor é maior do que a soma dos dois menores!')
# Falta diferenciar que o maior valor está duplicado, e que não forma triangulo
