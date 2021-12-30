terms = int(input(('Digite o número de termos que você quer: ')))
y = 1
z = 0
c = 0

while c < terms:
    x = y + z
    print(z, end=' » ')
    z = y
    y = x
    c += 1
print('FIM')