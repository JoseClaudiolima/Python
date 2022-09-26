n1 = int(input(f'Digite um número: '))
n2 = int(input(f'Digite um número: '))
n3 = int(input(f'Digite um número: '))
if (n1 > n2) and (n1 > n3):
    print(f'1° valor, {n1} é o maior valor!')
elif (n2 > n1) and (n2 > n3):
    print(f'2° valor, {n2} é o maior valor!')
elif (n3 > n1) and (n3 > n2):
    print(f'3° valor, {n3} é o maior valor!')
else:
    print(f'\nO maior valor, está presente em mais de uma variável')
