li = []
ag = ['vertebrado', 'ave', 'carnivoro']
pb = ['vertebrado', 'ave', 'onivoro']
vc = ['vertebrado', 'mamifero', 'herbivoro']
hm = ['vertebrado', 'mamifero', 'onivoro']
pg = ['invertebrado', 'inseto', 'hematofago']
lg = ['invertebrado', 'inseto', 'herbivoro']
sg = ['invertebrado', 'anelideo', 'hematofago']
mh = ['invertebrado', 'anelideo', 'onivoro']
for i in range(0, 3):
    n = str(input())
    li.append(n)
if li == ag:
    print('aguia')
elif li == pb:
    print('pomba')
elif li == hm:
    print('homem')
elif li == vc:
    print('vaca')
elif li == pg:
    print('pulga')
elif li == lg:
    print('lagarta')
elif li == sg:
    print('sanguessuga')
else:
    print('minhoca')
