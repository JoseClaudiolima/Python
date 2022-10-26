from os import system
system('cls') or None


nome1 = input(f'Digite o seu nome: ')
media1 = float(input(f'Digite o valor da média de {nome1}: '))
if media1 <7:
    situação = 'Reprovado!'
else:
    situação = 'Aprovado!'
dados = {'nome': nome1  ,'media':media1 ,'situação':situação}
system('cls') or None

