from os import system
array = []


def verificação(x):
    while x.isnumeric() is False or int(x) in array:
        print(f'É para digitar um V-A-L-O-R que já não foi digitado antes!')
        x = input(f'Digite um valor: ')
    return x


while True:
    system('cls') or None
    entrada = input(f'Digite um valor: ')
    entrada = verificação(entrada)
    array.append(int(entrada))
    while True:
        laço = input(f'Deseja continuar? [S/N] ').upper()
        if laço in 'SN':
            break
    if laço.upper() == 'N':
        break
print(f'Você digitou os valores: {array}')
