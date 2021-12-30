num = int(input('Digite um número: '))
cont = 0
for c in range(1,num+1):
    if num % c == 0:
        print('\033[1;33m{}\033[m'.format(c), end=' ')
        cont = cont + 1
    else:
        print('{}'.format(c), end=' ')

if cont == 2:
    print('\nO número {} foi divisível por {} vezes \nE por isso é um número primo!'.format(num, cont))
else:
    print('\nO número {} foi divisível por {} vezes \nE por isso não é um número primo!'.format(num, cont))
