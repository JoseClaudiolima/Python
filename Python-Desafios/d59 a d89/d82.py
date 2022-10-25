from array import array
from os import system
system('cls') or None

array = []
par = []
impar = []
while True:
    entrada = input(f'Digite um numero: ')
    while entrada.isnumeric() is False or int(entrada) in array:
        entrada = input(f'Digite um numero ainda não digitado: ')

    entrada = int(entrada)
    array.append(entrada)
    if entrada % 2 == 0:
        par.append(entrada)
    else:
        impar.append(entrada)

    loop = input(f'Deseja continuar? ')
    while loop not in 'SsNn':
        loop = input(f'Deseja continuar? [S/N]')
    if loop in 'Nn':
        system('cls') or None
        break
print(f'A lista completa é {array}')
print(f'A lista par é {par}')
print(f'A lista impar é {impar}')
