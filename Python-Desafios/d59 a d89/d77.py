from os import system
system('cls') or None

tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
         'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for i in range(len(tupla)):
    print(f'Na palavra {tupla[i]}, temos ', end='')
    for j in range(len(tupla[i])):
        if tupla[i][j].upper() in 'AEIOU':
            print(tupla[i][j].lower(), end=' ')
    print()
