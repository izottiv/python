nome = ['adalberto', 'roger', 'adadada', 'enzo']
idade = [12, 14, 25, 10]
h = 0
idd = 0
for i in range(len(idade)):
    if idade[i] > h:
        h = idade[i]
        idd = i
    else:
        print(nome[idd])
