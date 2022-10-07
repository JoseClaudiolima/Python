import os
os.system('cls') or None

n1 = int(input(f'Digite o primeiro numero:\t'))
n2 = int(input(f'Digite o segundo numero:\t'))

if (n1 > n2):
    print(f'{n1} é maior que {n2}')
elif (n2 > n1):
    print(f'{n2} é maior que {n1}')
else:
    print(f'Valores iguais!')
