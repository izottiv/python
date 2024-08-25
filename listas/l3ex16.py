h = m = s = sh = sm = n = pm = ph = 0
for i in range(1, 2001):
    sexo = int(input('Qual seu sexo ? (1 = homem, 2 = mulher) '))
    resposta = int(input('Gostou do produto ? (1 = Sim, 2 = Não) '))
    if sexo == 1:
        h += 1
        if resposta == 1:
            sh += 1
        elif resposta == 2:
            n += 1
    elif sexo == 2:
        m += 1
        if resposta == 1:
            sm += 1
        elif resposta == 2:
            n += 1
if m != 0:
    pm = (sm/m)*100
if h != 0:
    ph = (sh/h)*100
print('Número de pessoas que responderam sim: {}'.format(sm+sh))
print('Número de pessoas que responderam não: {}'.format(n))
print('Porcentagem de pessoas do sexo feminino que responderam sim: {}'.format(pm))
print('Porcentagem de pessoas do sexo masculino que responderam sim: {}'.format(ph))
