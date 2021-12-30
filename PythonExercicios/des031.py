print('Olá!\nVou te ajudar a calcular o valor de sua passagem!')
dist = float(input('Digite a distância da sua viagem: \n'))
if dist<=200:
    print('O valor da sua passagem será de R${:.2f}.'.format(dist*0.50))
else:
    print('O valor de sua passagem será de R${:.2f}.'.format(dist*0.45))
