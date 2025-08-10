ent1 = input()
ent2 = input()
ent3 = input()

if ent1 == 'vertebrado':
    if ent2 == 'ave':
        if ent3 == 'carnivoro':
            print('aguia')
        elif ent3 == 'onivoro':
            print('pomba')
    elif ent2 == 'mamifero':
        if ent3 == 'onivoro':
            print('homem')
        elif ent3 == 'herbivoro':
            print('vaca')
elif ent1 == 'invertebrado':
    if ent2 == 'inseto':
        if ent3 == 'hematofago':
            print('pulga')
        elif ent3 == 'herbivoro':
            print('lagarta')
    elif ent2 == 'anelideo':
        if ent3 == 'hematofago':
            print('sanguessuga')
        elif ent3 == 'onivoro':
            print('minhoca')
