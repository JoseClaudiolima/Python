from os import system
system('cls') or None

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatrorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = -1
while n < 0 or n > 20:
    n = int(input(f'Digite um valor: '))

print(f'Você digitou o número {tupla[n]}')
