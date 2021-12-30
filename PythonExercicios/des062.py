first = int(input('Digite o primeiro termo da P.A: '))
rason = int(input('Digite a razão da P.A: '))
pa = first
c = 1
final = 10
terms = 1
while terms != 0:
    while c <= final:
        print(pa, end=' -» ')
        pa += rason
        c += 1
    print('Pausa')
    terms = int(input('Quantos termos você quer mostrar a mais? '))
    final += terms
print('Ok! \nProgressão finalizada com {} termos.'.format(final))