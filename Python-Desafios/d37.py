# leia nmr
# usuario escolhe base de conversão

nmr = int(input(f'Escolha um número para ser convertido:\t'))
n_ini = nmr
empty = ''

escolha = int(input(f'''\nEscolha qual conversão deseja para o número {nmr}
1 para binário
2 para octal
3 para hexadecimal
'''))

res = []
if escolha == 1:
    while (nmr >= 2):

        res.append(str(nmr % 2))
        nmr = nmr//2

    res.append(str(nmr % 2))
    print(f'\n{n_ini} em binário é {empty.join(res)}')
