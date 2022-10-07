import os  # limpa terminal
from random import randint, randrange  # nmr aleatorio
from time import sleep  # freeza o terminal
os.system('cls') or None

# 2
num = int(input(f'Digite um valor:\t'))
nini = num

if num < 0:
    print("Não existe fatorial de numero negativo")

elif num == 0 or num == 1:
    fact = 1

else:
    fact = 1
    while (num > 1):
        fact *= num
        num -= 1

print(f'O fatorial de {nini} é {fact}')
sleep(3)

# 3
os.system('cls') or None

c = int(input(f'Digite o valor que irá pegar emprestrado:\t'))
t = int(input(f'Digite o tempo que terá para pagar o empréstimo:\t'))

while c < 0 or t < 0:
    c = int(input(f'Digite o valor que irá pegar emprestrado:\t'))
    t = int(input(f'Digite o tempo que terá para pagar o empréstimo:\t'))


i = 0.069
if t < 12:
    i = 0.0714
elif t < 24:
    i = 0.0921
else:
    i = 0.1246

print(f'O valor a ser pago dentro de {t} meses, será {c*(1+i)**t:.2f}')

# 4
os.system('cls') or None

random = randint(1, 10)
chute = -1
tentativa = 1
chute = int(input(
    f'Tente acertar o número aleatório,é sua {tentativa}° tentativa:\t'))

while chute < 1 or chute > 10:
    chute = int(input(f'Tente novamente, é de 1 a 10:\t'))

while (chute != random):
    tentativa += 1
    if tentativa > 3:
        print(f'Ultrapassou de 3 tentativas, você P-E-R-D-E-U!!')
        break

    chute = int(
        input(f'Tente acertar o número aleatório,é sua {tentativa}° tentativa:\t'))
    while chute < 1 or chute > 10:
        chute = int(input(f'Tente novamente, é de 1 a 10:\t'))

else:
    print(f'Acertou na {tentativa}, o valor era {random}!')
