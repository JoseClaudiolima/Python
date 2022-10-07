frase = input('Digite uma frase ae:\n').strip()
print(f'\nTem {frase.upper().count("A")} vezes a letra A.')
print(f'O primeiro "A" está na posição: {frase.upper().find("A")}.')
print(f'O ultimo "A" está na posição: {frase.upper().rfind("A")}.')
