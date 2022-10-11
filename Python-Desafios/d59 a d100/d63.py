from os import system
system('cls') or None


esc = int(
    input(f'Escolha quantos elementos da sequencia de fibonacchi serão mostrados: '))

fibo1 = 0
fibo2 = 1
'''
for i in range(esc):

    print(fibo1)
    print(fibo2)
    fibo1 += fibo2
    fibo2 += fibo1

'''
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,


if esc == 1:
    print(0)
elif esc == 2:
    print(0)
    print(1)
else:
    array = [0, 1]
    print(0)
    print(1)
    n = 2
    while n != esc:
        fibo1 = array[n-2]+array[n-1]
        array.append(fibo1)
        print(fibo1)
        n += 1
