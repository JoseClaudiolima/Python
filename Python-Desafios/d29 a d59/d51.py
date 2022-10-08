from os import system
system('cls') or None

n1 = int(input(f'Digite o primeiro termo de uma PA:\t'))
r = int(input(f'Digite a razão desta PA:\t'))

for i in range(1, 11):
    print(f'{n1+r} ', end='--> ')
    n1 += r
print('ACABOU')
