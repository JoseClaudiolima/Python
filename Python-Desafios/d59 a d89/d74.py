from os import system
from random import randint
system('cls') or None

numeros = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10))

print(f'Os valores sorteados foram: ', end='')
for n in range(len(numeros)):
    print(f'{numeros[n]} ', end='')

print(
    f'\nO maior valor sorteado foi {max(numeros)} e o menor valor foi {min(numeros)}.')
