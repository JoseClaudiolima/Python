from os import system
system('cls') or None


tuplas = ("PALMEIRAS", "Internacional", "Corinthians", "Flamengo", "Fluminense", "Athletico-PR", "Atlético-MG", "América-MG", "Botafogo",
          "Fortaleza", "Santos", "São Paulo", "Chapeconse", "Goiás", "Coritiba", "Ceará", "Cuiabá", "Atlético-GO", "Avaí", "Juventude")

print('-='*40)
print(f'Lista do brasileirão: {tuplas}')
print('-='*40)
print(
    f'Os cinco primeiros são: {tuplas[0:5]}')
print('-='*40)
print(
    f'Os 4 últimos são: {tuplas[-4:]}')
print('-='*40)
print(f'Chapecoense está na posição: {tuplas.index("Chapeconse")+1}°')
