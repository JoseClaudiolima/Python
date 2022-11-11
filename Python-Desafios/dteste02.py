from os import system
system('cls') or None

a = input('Numero 1: ')
b = input('Numero 2: ')
dict = {
    'Erro' : 'Erro! O Erro foi',
    'vermelho' : '\033[0;31m',
    'azul' : '\033[0;34m',
    'limpar' : '\33[m'
}
try:
    r = int(a) / int(b)

except (ValueError,TypeError):
    print(dict['vermelho'],dict['Erro'],f'dos tipos que vc digitou!',dict['limpar'])

except ZeroDivisionError:
    print(dict['vermelho']+dict['Erro']+' porque vc tentou dividir um número por zero!',dict['limpar'])

except KeyboardInterrupt:
    print(dict['vermelho'],dict['Erro'],f'porque o usuário não digitou nenhum dado!',dict['limpar'])

except Exception as erro:
    print(dict['vermelho'],dict['Erro'],f'de tipo {erro.__cause__}',dict['limpar'])

else:
    print(f'\033[0;34mA divisão entre {a} e {b} é {r:.2f}\33[m')