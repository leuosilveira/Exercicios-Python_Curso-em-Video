s = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        s = s + num
        cont = cont +1
if s == 0:
    print('Não há números pares entre os números digitados.')
else:
    print('Você digitou {} número(s) pare(s) e a soma entre eles é {}'.format(cont, s))
