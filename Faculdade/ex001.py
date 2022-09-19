n1 = int(input(f'Digite um valor: '))
n2 = int(input(f'Digite outro valor: '))
if n1 > n2:
    print(f'{n1} é maior que {n2}')
else:
    print(f'{n1} é menor que {n2}')
if n1 > 1:
    print(f'{n1} é maior que 1')
    if n1 > 2:
        print(f'{n1} é maior que 2')
        if n1 > 3:
            print(f'{n1} é maior que 3')

elif n1 > 1:
    print(f'\n{n1} é maior que 1')
elif n1 > 2:
    print(f'\n{n1} é maior que 2')
elif n1 > 3:
    print(f'\n{n1} é maior que 3')
