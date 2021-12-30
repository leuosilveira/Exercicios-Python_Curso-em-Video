num = int(input('Escolha um número e te mostrarei a tabuada dele: '))

for c in range(0, 11):
    print('{} x {} = {}'.format(num, c, (num * c)))
