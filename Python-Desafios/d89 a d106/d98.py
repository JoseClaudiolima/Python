from os import system
from time import sleep
system('cls') or None

def cabecalho():
        print('-='*20)
        print(f'Contagem de 1 até 10 de 1 em 1')
        i=1
        while i <11:
            sleep(.3)
            print(i,end=' ',flush=True)
            i+=1
        print('FIM!')

        print('-='*20)
        print(f'Contagem de 10 até 1 de 2 em 2')
        i=10
        while i >=0:
            sleep(.3)
            print(i,end=' ',flush=True)
            i-=2
        print('FIM!')
        print('-='*20)


def contagem(a,b,p):
    if p == 0:
        p=1

    if p <0:
        p = abs(p)

    if a > b: #decrescente, inicio >fim
        print('-='*20)
        print(f'Contagem de {a} até {b} de {p} em {p}')
        while a >=b:
            print(a,end=' ')
            a -=p


    elif a < b:
         print('-='*20)
         print(f'Contagem de {a} até {b} de {p} em {p}')
         while a <=b:
            print(a,end=' ')            
            a +=p

         print('FIM!')

cabecalho()
print()
print('Agora é sua vez de personalizar a contagem!')
n1 = int(input(f'Inicio: '))
n2 = int(input(f'Fim: '))
p = int(input(f'Passo: '))
contagem(n1,n2,p)