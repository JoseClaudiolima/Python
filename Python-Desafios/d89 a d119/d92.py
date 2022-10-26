from os import system
import datetime
system('cls') or None
now = datetime.datetime.now()
#print(now.year)

dict = {}
dict['nome'] = input(f'Nome: ')
dict['idade'] = now.year - int(input(f'Ano de Nascimento: '))
dict['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dict['ctps'] != 0:
    dict['contratação'] = int(input(f'Ano de contratação: '))
    dict['salário'] = int(input(f'Salário: R$ '))
    print('-='*30)
    print(f'''Nome: {dict['nome']}\nIdade: {dict['idade']}\nCTPS: {dict['ctps']}\nContratação: {dict['contratação']}\nSalário: {dict['salário']}\nAposentadoria: {(dict['contratação'] -now.year)+ dict['idade']  +45}''')
else:
    print('-='*30)
    print(f'''Nome: {dict['nome']}\nIdade: {dict['idade']}\nCTPS : {dict['ctps']}''')

