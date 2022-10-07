import os
os.system('cls') or None


def inverte():

    length = len(res)-1
    finalres = []

    while length >= 0:
        finalres.append(res[length])
        length += -1

    return finalres


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
    print(f'\n{n_ini} em binário é {empty.join(inverte())}')


elif escolha == 2:
    while (nmr >= 8):

        res.append(str(nmr % 8))
        nmr = nmr // 8

    res.append(str(nmr % 8))
    print(f'\n{n_ini} em octal é {empty.join(inverte())}')


elif escolha == 3:
    alfanumber = [10, 'A', 11, 'B', 12, 'C', 13, 'D', 14, 'E', 15, 'F']
    while (nmr >= 16):
        if nmr % 16 >= 10:
            res.append(str(alfanumber[alfanumber.index(nmr % 16)+1]))
        else:
            res.append(str(nmr % 16))
        nmr = nmr // 16

    if nmr % 16 >= 10:
        res.append(str(alfanumber[alfanumber.index(nmr % 16)+1]))
    print(f'\n{n_ini} em hexadecimal é {empty.join(inverte())}')
