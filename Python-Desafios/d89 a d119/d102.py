from os import system
system('cls') or None


def fat(number,show=False):
    """
    number será o numero calculado
    show é opcional para mostrar a conta
    return retorna o fatorial do numero
    """
    if number ==0 or number == 1:
        return number
    if show==True:
        print(number)
        return number * fat(number-1,show=True)
    return number * fat(number-1)


n1 = int(input(f'Fatorial de: '))
print(fat(n1,show=True))
print(help(fat))