from os import system
system('cls') or None

dict = {}
array =[]
while True:
    gols = []
    print('--'*30)
    dict['nome'] = input(f'Nome do Jogador: ')

    qtdgols = input(f'Quantas partida jogou? ')
    while qtdgols.isnumeric() is False:
            qtdgols = input(f'Quantas partida Joelson jogou? ')
    qtdgols = int(qtdgols)

    dict['partidas'] = qtdgols
    for k in range(dict['partidas']):
        gols.append(int(input(f'Quantos gols na partida {k+1}? ')))
    dict['gols'] = gols.copy()

    array.append(dict.copy())

    looping = input(f'Deseja continuar? [S/N]').upper()
    while looping not in 'SsNn':
        looping = input(f'Deseja continuar? [S/N]').upper()
    if looping in 'Nn':
        break

system('cls') or None
print('-='*60)
bugprint = ['nome','gols','total']
print(f'cod {str(bugprint[0]):<20}{str(bugprint[1]):<16}{str(bugprint[2])}')
print('--'*60)

for k in range(len(array)):
    #print(k,array[k]['nome'].ljust(20,' '),(array[k]['gols']),''.ljust(16,' '),sum(array[k]['gols']))
    bug='"'+ str(array[k]['gols'])+'"'
    print(bug, end=' ')
    print(k, end=' ')
    print(array[k]['nome'].ljust(20,' '), end=' ')
    print(array[k]['gols'],end=f'{" "*(len(bug))}')
    print(sum(array[k]['gols']))