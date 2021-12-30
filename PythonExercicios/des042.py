print('Olá! \nVou te ajudar a identificar se três seguimentos de retas podem formar um triângulo e qual o tipo.')
print('- - ' * 20)
r1 = float(input('Por favor, digite o valor da primeira reta: '))
r2 = float(input('Por favor, digite o valor da segunda reta: '))
r3 = float(input('Por favor, digite o valor da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM formar um triângulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima NÃO PODEM formar um triângulo.')
