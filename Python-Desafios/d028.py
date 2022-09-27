from random import randrange
from time import sleep
n1 = randrange(1, 6)
innum = int(input(f'Tente acertar o numero escolhido, [1 a 5]: '))
print(f'Processando... ... ...')
sleep(2)
if n1 == innum:
    print(f'Você acertou!')
else:
    print(f'Você errou!')
