from os import system
system('cls') or None

dict = {}
dict['nome'] = input(f'Nome do Jogador: ')
while True:
    partidas = input(f'Quantas partidas Joelson jogous? ')
    if partidas.isnumeric():
        break
partidas = int(partidas)
gols = []
for j in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {j+1}? ')))
dict['gols'] = gols
dict['total'] = 6
system('cls') or None
print('-='*30)
print(f'O campo nome tem o valor',dict['nome'])
print(f'O campo gols tem o valor',dict['gols'])
print(f'O campo total tem o valor',dict['total'])
print(dict)
print('-='*30)

t=0
print(f'O jogador',dict['nome'],'jogou',len(dict['gols']), 'partidas.')
for i in range (len(dict['gols'])):
    print(f'    => Na partida {[i+1]}, fez,',dict['gols'][i],'gols.')
    t+=dict['gols'][i]
print(f'Foi um total de {t} gols.')