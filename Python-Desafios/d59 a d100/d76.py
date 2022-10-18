from os import system
from random import randint
system('cls') or None

listagem = ('Lápis', randint(1, 150), 'Borracha', randint(1, 150), 'Caderno', randint(1, 150), 'Estojo', randint(1, 150), 'Transferidor', randint(1, 150), 'Compasso', randint(1, 150), 'Mochila', randint(1, 150), 'Canetas', randint(
    1, 150), 'Livro', randint(1, 150))
print('-' * 40)
print(f'{"LISTAGEM DE PRECOS":^40}')
print('-' * 40)

for i in range(len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<30}', end='')
    else:
        print(f'R${listagem[i]:>7.2f}')
print('-' * 40)
