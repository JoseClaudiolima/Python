from random import choice
n1 = int(input(f'Primeiro número: '))
n2 = int(input(f'Segundo número: '))
n3 = int(input(f'Terceiro número: '))
n4 = int(input(f'Quarto número: '))

lista = [n1, n2, n3, n4]
print(f'O aluno escolhido foi {choice(lista)}')
