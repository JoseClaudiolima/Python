from os import system
from datetime import date
system('cls') or None

def voto(a):
    if a <16:
        print(f'Não pode votar')
    elif a <=17:
        print(f'Voto Opcional')
    elif a>=18:
        print(f'Você é OBRIGADO a votar, não tem liberdade de não ir para as urnas.')


anoatual = date.today().year
idade = anoatual - int(input(f'Em que ano vc nasceu? '))
print(idade)
voto(idade)