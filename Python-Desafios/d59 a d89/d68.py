from os import system
from time import sleep
from random import randint
system('cls') or None

consec = 0

while True:
    pi = 'a'
    print('-=' * 20)
    print(f'VAMOS JOGAR PAR OU ÍMPAR')
    print('-=' * 20)

    while pi not in 'PI':
        pi = input(f'Par ou Ímpar? [P/I] ').strip().upper()
    n = int(input(f'Digite um valor [1 a 5] : '))
    nbot = randint(1, 6)

    print(
        f'\nVocê jogou {n} e o computador {nbot}.\nTotal deu {n + nbot}.', end=' ')

    if (n + nbot) % 2 == 0:
        print('PARES ganharam!')
        if pi == 'P':
            print(f'\nVocê venceu!\nVamos jogar novamente...')
            consec += 1
        elif pi == 'I':
            print(f'\nGAME OVER! Você venceu {consec} vezes.')
            break
    else:
        print('ÍMPARES ganharam!')
        if pi == 'I':
            print(f'\nVocê venceu!\nVamos jogar novamente...')
            consec += 1
        elif pi == 'P':
            print(f'\nGAME OVER! Você venceu {consec} vezes.')
            break

    sleep(6)
    system('cls') or None
