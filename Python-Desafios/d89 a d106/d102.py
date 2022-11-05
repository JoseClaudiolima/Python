from os import system
system('cls') or None


def fat(n,show=False):
    """
    number será o numero calculado
    show é opcional para mostrar a conta
    return retorna o fatorial do numero
    """
    f=1
    for c in range(n,0,-1):
        if show:
            print(c,end='')
            if c>1:
                print(' x ',end= '')
            else:
                print(' = ',end='')
        f *= c
    return f


n1 = int(input(f'Fatorial de: '))
print(fat(n1,show=True))
help(fat)