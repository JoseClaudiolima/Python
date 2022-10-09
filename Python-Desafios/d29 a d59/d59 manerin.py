from time import sleep
from random import randint
from os import system

system('cls') or None

n1 = randint(1, 100)
n2 = randint(1, 100)
print(f'O computador escolheu: {n1} e {n2}.')

esc = int(input(f'''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do Programa\nFaça a sua escolha: '''))

array = [n1, n2]
arraystr = [str(n1), ' e ', str(n2)]
empty = ''
while esc != 5:
    s = 0
    m = 1

    if esc == 1:  # somar
        for i in range(len(array)):
            s += array[i]
        print(f'A soma dos valores escolhidos é {s}.')

    if esc == 2:  # multiplicar
        for i in range(len(array)):
            m *= array[i]
        print(f'A multiplicação dos valores escolhidos é {m}.')

    if esc == 3:  # maior
        for i in range(len(array)-1):
            maior = array[0]
            if array[i+1] > maior:
                maior = array[i+1]
        print(f'O maior número é {maior}.')

    if esc == 4:  # add numero
        n3 = randint(1, 100)

        array.append(n3)
        arraystr.append(' e ')
        arraystr.append(str(n3))

        arraystr[len(arraystr)-4] = ', '

    sleep(4)
    system('cls') or None
    print(f'O computador escolheu: {empty.join(arraystr)}')
    esc = int(input(f'''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do Programa\nFaça a sua escolha: '''))

print(f'Obrigado por testar o programa :)')
