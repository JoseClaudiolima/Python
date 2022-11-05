from os import system
system('cls') or None

#<desconhecido>
#0gols

def ficha(nome=0,gols=0):
    if nome ==0 or nome == '':
        nome = '<desconhecido>'
    if gols == '' or gols.isnumeric() is False:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome = input(f'Nome do Jogador: ').replace(' ','')
gols = input(f'Número de gols: ').replace(' ','')
ficha(nome,gols)