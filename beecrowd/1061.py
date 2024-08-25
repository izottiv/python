a, d = map(str, input().split())
d = int(d)
h, m, s = map(int, input().split(':'))
a, df = map(str, input().split())
df = int(df)
hf, mf, sf = map(int, input().split(':'))
dd = df-d
ht1 = h*60 + m
ht2 = hf*60 + mf
if ht1 < ht2:
    tempo = ht2 - ht1
elif ht2 < ht1:
    tempo = ((24*60) - ht1) + ht2
elif ht1 == ht2:
    tempo = (24*60)

horas = tempo // 60
minutos = tempo % 60
segundos = minutos // 60
print('{} dia (s)'.format(d))
print('{} hora (s)'.format(horas))
print('{} minuto (s)'.format(minutos))
print('{} segundo (s)'.format(segundos))
