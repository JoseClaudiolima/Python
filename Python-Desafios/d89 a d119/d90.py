from os import system
system('cls') or None

dic = {}
dic['nome'] = input(f'Digite o seu nome: ')
dic['media'] = float(input(f'Digite a sua média: '))

if dic['media'] <7:
    dic['situação'] = 'Reprovado!'
else:
    dic['situação'] = 'Aprovado!'

print(f'Nome é ',dic['nome'])
print(f'Média é ',dic['media'])
print(f'Situação é ',dic['situação'])