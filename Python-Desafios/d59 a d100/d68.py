from os import system
from time import sleep
from random import randint
system('cls') or None

consec = 0
while True:

    print('-=' * 20)
    print(f'VAMOS JOGAR PAR OU ÍMPAR')
    print('-=' * 20)

    pi = input(f'Par ou Ímpar? [P/I] ')
    n = int(input(f'Digite um valor [1 a 5] : '))
    nbot = randint(1, 6)

    print(
        f'\nVocê jogou {n} e o computador {nbot}.\nTotal deu {n + nbot}.', end=' ')

    if (n + nbot) % 2 == 0:
        print('PARES ganharam!')
        if pi.strip().upper() == 'P':
            print(f'\nVocê venceu!\nVamos jogar novamente...')
            consec += 1
        elif pi.strip().upper() == 'I':
            print(f'\nGAME OVER! Você venceu {consec} vezes.')
            break
    else:
        print('ÍMPARES ganharam!')
        if pi.strip().upper() == 'I':
            print(f'\nVocê venceu!\nVamos jogar novamente...')
            consec += 1
        elif pi.strip().upper() == 'P':
            print(f'\nGAME OVER! Você venceu {consec} vezes.')
            break

    sleep(6)
    system('cls') or None
