from os import system
system('cls') or None

# 1
'''
nome = input(f'Digite o seu nome: ')
cpf = input(f'Digite o seu cpf: ')
rg = input(f'Digite o seu rg: ')
sexo = input(f'Digite o seu sexo [M/F]: ').upper()
while sexo not in 'MF':
    sexo = input(f'Digite o seu sexo [M/F]: ').upper()
idade = int(input(f'Digite o seu idade: '))

if sexo == 'M':
    print(f'{nome} irá se aposentar com {idade+65}, caso não tenha trabalhado ainda, e comesse no próximo ano')
else:
    print(f'{nome} irá se aposentar com {idade+60}, caso não tenha trabalhado ainda, e comesse no próximo ano')
'''

# 2
print("Aparantemente, você não tem cadastro ainda, faça o seu agora!")
login = input(f'Cadastre o seu login: ').upper()
while login.isalpha() is False:
    if login.isalnum() and login[0].isnumeric is False:
        break
    print(f'Apenas algarismos alfanúmeros, e não pode começar com números!')
    login = input(f'Cadastre o seu login: ').upper()
