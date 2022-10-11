from os import system
from random import randint, choice
system('cls') or None

genero = ['F', 'M']
usu = 'a'
m18 = h = f = f18 = c = 0
while True:
    i = randint(14, 30)
    sex = choice(genero)

    if usu == 'N':
        break

    if i >= 18:
        m18 += 1
    if sex == 'M':
        h += 1
    else:
        f += 1
        if i <= 18:
            f18 += 1

    c += 1

    usu = input(
        f'Houve {c} cadastros até agora.\nDeseja continuar? [S/N]\t').strip().upper()[0]
    while usu != 'S' and usu != 'N':
        usu = input(
            f'Houve {c} cadastros até agora.\nDeseja continuar? [S/N]\t').strip().upper()[0]
    system('cls') or None

print(
    f'Pessoas maiores de 18: {m18} pessoas\nHomens cadastrados: {h} homens\nMulheres menor de 18 cadastradas: {f18} mulheres\n')
