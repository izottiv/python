from math import cos, tan, sin, radians
n = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} tem o SENO de {:.2f}'.format(n, sin(radians(n))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(n, cos(radians(n))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(n, tan(radians(n))))
