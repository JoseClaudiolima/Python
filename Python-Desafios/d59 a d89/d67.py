from os import system
from time import sleep
system('cls') or None

while True:
    n = int(input(f'Quer ver a tabuada de qual valor?: '))

    if n < 0:
        break

    print('-'*40)
    for i in range(10):
        print(f'{n} * {i+1} = {n*(i+1)}')
    print('-'*40)

    sleep(3)
    system('cls') or None

print(f'Programa finalizado!')
