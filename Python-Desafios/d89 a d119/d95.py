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

    looping = input(f'Deseja continuar? [S/N] ')
    while looping not in 'SsNn':
        looping = input(f'Deseja continuar? [S/N] ')
    if looping in 'Nn':
        break

system('cls') or None
print('-='*40)
bugprint = ['nome','gols','total']
print(f'cod {str(bugprint[0]):<20}{str(bugprint[1]):<16}{str(bugprint[2])}')
print('--'*40)

for k in range(len(array)):
    bug=''+ str(array[k]['gols'])+''
    print(k, end='   ')
    print(array[k]['nome'].ljust(19,' '), end=' ')
    print(f'{str(bug):<17}',end='')
    print(sum(array[k]['gols']))

while True:
    print('-='*40)
    decisao = input(f'Mostrar dados de qual jogador? (999 para parar): ')
    while decisao.isnumeric() is False or int(decisao) > len(array)-1 and int(decisao) !=999:
            decisao = input(f'Mostrar dados de qual jogador? (999 para parar): ')
    if int(decisao) ==999:
        break
    print(f'LEVANTAMENTO DO JOGADOR',array[int(decisao)]['nome'])
    for k in range(len(array[int(decisao)]['gols'])):
        print(f'No jogo {k+1} fez',array[int(decisao)]['gols'][k],'gols.')
print(f'\nOBRIGADO, VOLTE SEMPRE!')