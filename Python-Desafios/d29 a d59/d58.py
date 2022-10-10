from os import system
from random import randrange
from time import sleep
system('cls') or None

n1 = randrange(1, 10)
innum = -1
tentativa = 1

while innum != n1:
    system('cls') or None
    innum = int(input(f'Tente acertar o numero escolhido, [1 a 10]: '))
    print(f'Processando...')
    sleep(0.5)
    print(f'Processando... ...')
    sleep(0.5)
    print(f'Processando... ... ...')

    if n1 == innum:
        print(f'Você acertou, e foi na sua {tentativa}° tentativa.')
    else:
        if innum > n1:
            print(
                f'Você errou, o número é menor, e foi na sua {tentativa}° tentativa.')
        else:
            print(
                f'Você errou, o número é maior, e foi na sua {tentativa}° tentativa.')
    tentativa += 1
    sleep(2)
