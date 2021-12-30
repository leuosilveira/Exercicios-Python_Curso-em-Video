first = int(input('Digite o primeiro número da P.A: '))
rason = int(input('Digite a Razão da P.A: '))
pa = first
c = 0
print('Veja abaixo os 10 primeiros termos desta P.A:')
while c < 10:
    print(pa, end='')
    print(' -» 'if c < 9 else '', end='')
    pa = pa + rason
    c += 1
