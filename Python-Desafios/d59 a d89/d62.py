from os import system
system('cls') or None

n1 = int(input(f'Digite o primeiro termo de uma PA:\t'))
r = int(input(f'Digite a razão desta PA:\t'))

d = 1
while d != '0':
    for i in range(1, 11):
        print(f'{n1+r} ', end='--> ')
        n1 += r

    d = input(f'''
[0] para Sair
[''] Digite qualquer outra coisa, para mostrar os próximos 10 numeros\nEscolha: ''')
    system('cls') or None
