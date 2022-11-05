from os import system
system('cls') or None


def leiaint(textinput):
    numero = input(textinput)
    while numero.isnumeric() is False:
        print('\033[31m','ERRO! Digite um número inteiro!','\033[m')
        numero = input(textinput)
    return int(numero)

n = leiaint('Digite um número: ')
print(f'Você digitou {n}')
