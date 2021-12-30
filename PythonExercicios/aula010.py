n1 = float(input('Digite sua primeira nota: \n'))
n2 = float(input('Digite a segunda nota: \n'))
m = (n1 + n2)/2
print('Sua média final é {:.1f}.'.format(m))
if m >= 6:
    print('Sua média foi satisfatória. PARABÉNS!')
else:
    print('Sua média não foi satisfatória. Sugiro que estude mais e tente novamente.')
#print('PARABÉNS!' if m >= 6 else 'ESTUDE MAIS')