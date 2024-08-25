h1, m1, h2, m2 = map(int, input().split())
ht1 = h1*60 + m1
ht2 = h2*60 + m2

if ht1 < ht2:
    tempo = ht2 - ht1
elif ht2 < ht1:
    tempo = ((24*60) - ht1) + ht2
elif ht1 == ht2:
    tempo = (24*60)

horas = tempo // 60
minutos = tempo % 60

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
