from os import system
from time import sleep
from random import randint
system('cls') or None

def maior(a):
    print('-='*30)
    print(f'Analise concluida!')
    for pos,valor in enumerate(a):
        sleep(0.3)
        print(valor,end=' ',flush=True)
        if pos ==0:
            nmaior = valor
        else:
            if valor > nmaior:
                nmaior = valor
                st = str(valor)
            elif valor == nmaior:
                st+= ' '+str(valor)
    print(f'Foram informador {len(a)} valores ao todo.')
    print(f'O(s) maior(es) valor(es) informado(s) foi {st}')
    print('-='*30)


array = []
c=0
while True:
    while True:
        system('cls') or None
        #n1 = input(f'Adicione um Numero: ')
        #while n1.isnumeric() is False:
        #    n1 = input(f'Numero: ')
        #n1= int(n1)
        n1 = randint(1,100)
        array.append(n1)

        #decisao = input(f'Deseja continuar? [S/N] ')
        #while decisao not in 'SsNn':
        #    print('Atenção')
        #    decisao = input(f'Deseja continuar? [S/N] ')
        #if decisao in 'Nn':
        #    break
        c+=1
        if c ==10:
            break

    c=0
    maior(array)
    array = []
    decisao = input(f'Deseja continuar? [S/N] ')
    while decisao not in 'SsNn':
        print('Atenção')
        decisao = input(f'Deseja continuar? [S/N] ')
    if decisao in 'Nn':
        break