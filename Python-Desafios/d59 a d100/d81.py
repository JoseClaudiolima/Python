from os import system
system('cls') or None

array = []
while True:
    entrada = input(f'Digite um valor: ')
    while entrada.isnumeric() is False or int(entrada) in array:
        entrada = input(
            f'Digite um valor númerico que ainda não foi digitado: ')

    array.append(int(entrada))
    simnao = input(f'Deseja continua?[S/N]:  ')
    while simnao not in 'SsNn':
        simnao = input(f'Deseja continua? Somente aceito [S/N]:  ')
    if simnao in 'nN':
        system('cls') or None
        break

array.sort(reverse=True)
print(f'Você digitou {len(array)} elementos.')
print(f'Os valores em ordem decrescente são {array}')
if 5 in array:
    print(f'O valor 5 está na posição {array.index(5)}')
else:
    print(f'Valor 5 não está na array.')
