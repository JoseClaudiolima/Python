a = input('Digite qualquer coisa ')

print(f'Sua mensagem é:"', a, '" e é do tipo primitivo:', {type(a)})

print('Sua mensagem só contém espaços? ', a.isspace())
print('Sua mensagem é um numero? ', a.isnumeric())
print('Sua mensagem é alfabético?', a.isalpha())
print('Sua mensagem é alfanumérica? ', a.isalnum())
print('Sua mensagem está em maiusculo?', a.isupper())
print('Sua mensagem está em minusculo?', a.islower())
print('Sua mensagem está capitalizada? ', a.istitle())
