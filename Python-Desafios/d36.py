# entrada valor casa, salario pessoa, anos a pagar
# calcule prestação mensal, prestação mensal não pode exceder 30% do salario da pessoa
sal = int(input(f'Digite o seu salário:\t'))
vcasa = int(input(f'Digite o valor da casa que deseja comprar:\t'))
tempo = int(input(f'Digite quantidade de anos a pagar a casa:\t'))

prestm = vcasa / tempo
if prestm > sal*0.3:
    print(f'\nInfelizmente, a prestação mensal é maior do que 30% do seu salário, desta forma não é possivel efetuar o empréstimo para a compra da casa!')
    print(f'{prestm:.2f}, {sal:.2f}, {sal * 0.3:.2f}')
else:
    print(
        f'Parabéns, você conseguirá fazer o empréstimo.\n A mensalidade será {prestm}, e não passa de 30% do seu salário, que é exatamente: {sal*0.3}')
