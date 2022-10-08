from os import system
system('cls') or None

n = int(input(f'Digite um número inteiro:\t'))

if n == 1:
    print(f'Não é primo')
elif n == 2 or n == 3 or n == 5 or n == 7:
    print(f'É número primo!')

elif n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
    print(f'É número primo!')
else:
    print(f'Não é número primo!')
