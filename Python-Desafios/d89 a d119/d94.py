from os import system
from random import randint
system('cls') or None

dict = {}
array = []
m=0
mulheres=''
while True:
    dict['nome'] = input(f'Nome: ')
    dict['genero'] = input(f'Genero: [M/F] ').upper()
    dict['idade'] = randint(18,40)
    array.append(dict.copy())

    if dict['genero'] in 'Ff':
        mulheres += dict['nome'] + ' '
    m += dict['idade']

    dict.clear()
    system('cls') or None

    looping = input(f'Quer continuar? [S/N] ')
    while looping not in 'SsNn':
        looping = input(f'Quer continuar? [S/N]')
    if looping in 'Nn':
        break



end_array = []
for i in range(len(array)):
    if array[i]['idade'] > m/len(array):
        end_array.append(array[i])

print('-='*30)
print(f'- O grupo tem {len(array)} pessoas.')
print(f'- A média de idade é de {m/len(array):.2f}')
print(f'As mulheres cadastradas foram: {mulheres}')
print(f'Lista das pessoas que estão acima da média de idade:')

for j in range(len(end_array)):
    print(end_array[j])
    