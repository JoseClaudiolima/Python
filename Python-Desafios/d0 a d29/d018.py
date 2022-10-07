from math import radians, sin, cos, tan

angulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print(
    f'O seno, cosseno e tangente de {angulo} é respectivamente: {seno:.2f}, {cos:.2f} e {tan:.2f}')
