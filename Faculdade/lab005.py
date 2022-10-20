from os import system
from time import sleep
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
system('cls') or None

print("Aparantemente, você não tem cadastro ainda, faça o seu agora!")
print(f'Atenção, o seu login não pode começar com números e ter espaços!')
login = input(f'Cadastre o seu login: ')
while login.isalnum() is False or login[0].isnumeric():
    print(f'Apenas algarismos alfanúmeros, e não pode começar com números nem ter espaços!')
    login = input(f'Cadastre o seu login: ').upper()

print(f'\nLogin cadastrado com sucesso!')


print(f'\nAgora vamos cadastrar a sua senha!')
print(f'Sua senha deverá ter no minimo 8 caracteres e um caractere especial.')
senha = input(f'Digite a sua senha: ')

while len(senha) < 8:
    print(f'Sua senha deverá ter no minimo 8 caracteres e um caractere especial.')
    senha = input(f'Digite a sua senha: ')
a = 0
while a == 0:
    for i in range(len(senha)):
        if senha[i] in '!@#$%¨&*()':
            a = 1

print(f'Senha cadastrada com sucesso!')
sleep(3)
system('cls') or None
ent = input(f'Entre com o seu Login: ')
if ent == login:
    ent = input(f'Entre com a sua Senha: ')
    if ent == senha:
        print(f'Bem vindo ao APP!')
    else:
        print(f'Senha Incorreta!')
else:
    print(f'Usuário não cadastrado!')


# 3
