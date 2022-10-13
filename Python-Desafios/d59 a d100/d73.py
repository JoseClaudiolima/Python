from os import system
system('cls') or None

tupla = ("PALMEIRAS", "Internacional", "Corinthians", "Flamengo", "Fluminense", "Athletico-PR", "Atlético-MG", "América-MG", "Botafogo",
         "Fortaleza", "Santos", "São Paulo", "Red Bull Bragantino", "Goiás", "Coritiba", "Ceará", "Cuiabá", "Atlético-GO", "Avaí", "Juventude")

print('-='*60)
print(f'Lista do brasileirão: {tupla}')
print('-='*60)
print(
    f'Os cinco primeiros são: {tupla[0]}, {tupla[1]}, {tupla[2]}, {tupla[3]} e {tupla[4]}')
print('-='*60)
print(f'Os 4 últimos são: {tupla[-4]},{tupla[-3]},{tupla[-2]} e {tupla[-1]}')
print('-='*60)
print(f'Chapecoense está na posição: {tupla.index(chapeconse)}')
