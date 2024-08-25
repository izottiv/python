PRODUTOS = ["Caneta Azul", "Caderno Espiral", "Mochila Escolar", "Calculadora Científica", "Lápis de Cor", "Borracha", "Agenda 2024", "Marcador Permanente", "Estojo",
            "Régua de 30cm", "Cola Bastão", "Apontador", "Livro de Matemática", "Tinta Guache", "Pasta de Arquivo"]
VALORES = [3.50, 18.90, 120.00, 45.00, 22.50, 2.00, 25.00,
           6.00, 15.00, 4.50, 3.00, 5.00, 35.00, 8.00, 12.00]
r = VALORES[0]
g = VALORES[0]
for i in range(15):
    if VALORES[i] > r:
        r = VALORES[i]
        idcaro = i
    if VALORES[i] < g:
        g = VALORES[i]
        idbarato = i
print(f'O produto mais caro é {PRODUTOS[idcaro]} e seu valor é {VALORES[idcaro]}')
print(f'O produto mais barato é {PRODUTOS[idbarato]} e seu valor é {VALORES[idbarato]}')
n = str(input('Digite o nome de um produto: '))
for i in range(15):
    if PRODUTOS[i] == n:
        print(f'seu valor é {VALORES[i]}')
