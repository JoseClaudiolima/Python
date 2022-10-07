km = float(input(f'Qual a quantidade de km percorrido por esse carro? '))
dias = int(input(f'Quantos dias você teve o carro alugado? '))
p = (60 * dias) + (0.15 * km)
print(f'\nA quantidade que deve pagar é: {p:.2f}')
